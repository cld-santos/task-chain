# Task chain POC

The intention on this project is to learn how to implement a task chain using python asyncio.
This process of learning will provide a very good foundation on how to work on asyncio.

## Project

I as a Place Manager,
Want to read a text file of addresses, break a text line in an Address Object, Geocode the address and save all the Address into a Database,
So I can plot these addresses in a map

In order to execute each task we can do it on step by step, but we are wasting the time waiting to get a file read, sending a http request or saving it to database, so the intention is to use asyncio to save that waiting time.


## Utility Tools

*create_fake_addresses:* let you create a defined number of address base on a list of words.

```
python utils/create_fake_addresses.py /home/project/task-chain/resources/words.txt 10000000
``` 
