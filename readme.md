# Amazon Asynchronous Prices Scraper

This is a simple asynchronous scraper for Amazon prices intended to be used as an Amazon Lambda function.

I wanted to figure out, how make use of concurrency in Python also in Amazon Lambda Functions.

It was tested using Python 3.10 Runtime.

## Usage

It makes use of [scrap.io](https://scrapeops.io) in order to avoid getting blocked by Amazon. (You can use it for free for up to 1000 requests per month). After your free account you have to set your API Key in the `SCRAPEOPS_API_KEY` ENV Variable.

I also added the handy `create_lambda.sh` script, which creates a zip file with all the dependencies and the code, which can be uploaded to Amazon Lambda (make sure to adapt to your `pip` version).

## Sample payload

```
[
  {
    "product_id": 1,
    "url": "https://www.amazon.com/dp/B08F14WY7L/",
    "name": "Yamaha Audio SR-B20A Sound Bar",
    "price": 0,
    "scrap_field": "a-offscreen",
    "created_at": "2023-06-17 4:00:26",
    "updated_at": "2023-06-26 3:01:38"
  }
]
```