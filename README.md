# simple-cntk-lstm
Very simple example of predicting sin(x)/x series with lstm using cntk.

It is created in response to [this request](https://github.com/Microsoft/CNTK/issues/647) in CNTK issues.

## How to run

1. Clone the repository
2. Open command prompt into the cloned folder
3. Run the following command:
`cntk configFile=lstm.cntk`.
If you do not like to see logs in the command prompt, then run:
`cntk configFile=lstm.cntk 1>out.txt 2>&1`.
It will dump all the logs into _out.txt_ file in that folder.
