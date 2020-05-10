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


## Execution Logs

### Async
1st - 269082 for 60 minutes meaning 74,745 TPS
2nd - started at 21:15:40 finish at 21:37:56
      200000 for 22 minutes meaning 151,515 TPS
      Reason: better control over http session and database pool

### Sync
1st - started at 22:21:35 finish at 22:54:18
      200000 for 33 minutes meaning 101,01

