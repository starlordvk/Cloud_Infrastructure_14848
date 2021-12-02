from pyspark import SparkConf, SparkContext

def split_func(file_contents):
    file_words = file_contents[1].split()
    file_words = filter(lambda word: word not in stop_words, file_words)
    return [(word, {file_contents[0]: 1}) for word in list(file_words)] 

def reduce_func(key,val):
    return {x: val.get(x, 0) + key.get(x, 0) for x in set(val) | set(key)}


conf = SparkConf()
spark_context = SparkContext.getOrCreate(conf=conf)
stop_words = ['they', 'she', 'he', 'it', 'the', 'as', 'is', 'and']

path = 'textfiles'
rdd = spark_context.wholeTextFiles(path)
words = rdd.flatMap(split_func)
counts = words.reduceByKey(reduce_func)
counts.take(5)
counts.saveAsTextFile("counts_file")