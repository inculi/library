# Library

Previously, many ebook libraries have been organized with folders based on topic or genre. While tags allow us to make some improvements on this system, we believe much more can be achieved.

The Inculi Library extracts the full text and metadata of each uploaded document, creating a [vector](https://arxiv.org/abs/1405.4053) representation of our document. This allows us to perform sentiment analysis, such as clustering, to group alike documents together. Because the full text of each document is extracted, the entire corpus is searchable using Elasticsearch.

## Requirements

- Apache Tika
- Elasticsearch
- Python3