from elasticsearch import Elasticsearch
from elasticsearch_dsl.connections import connections
from elasticsearch_dsl import Search
#https://my-deployment-f971ce.es.us-east-2.aws.elastic-cloud.com:9243

#connections.create_connection(hosts=['https://boilermake.es.us-east-2.aws.elastic-cloud.com:9243'], timeout=20)

client = Elasticsearch(hosts=['https://boilermake.es.us-east-2.aws.elastic-cloud.com:9243'], http_auth=('elastic', 'q7K7gb2mmq5Pn5D8KvFAGZGe'))

s = Search(using=client, index="course_data") \
    .filter("term", category="search") \
    .query("match", title="python")   \
    .exclude("match", description="beta")

s.aggs.bucket('per_tag', 'terms', field='tags') \
    .metric('max_lines', 'max', field='lines')

response = s.execute()

for hit in response:
    print(hit.meta.score, hit.title)

for tag in response.aggregations.per_tag.buckets:
    print(tag.key, tag.max_lines.value)




