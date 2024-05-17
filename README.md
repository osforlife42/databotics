# databotics

## Purpose 

data calculation pipeline for computation graph of unsynchronized data from multiple source. 

## Assumptions and Methodology 

1. The inputs as mentioned are unsynchronized and can come from different sources. most of them come in a constant rate. 

2. all the inputs, calculations and outputs are saved on timestamped dictionary called the `data pool`.  

3. to the `data pool` there are readers and writers. There can be only one writer to each key in the `data pool` and many readers to each key. There cannot exist a reader to a key without an existing writer to it. The readers, writers and `data pool` are static for simplicity. 

4. The methodology is to create a computation graph which is built into different computation blocks and then calculated effectively layer by layer until it is all computed. 

5. The computation for the entire graph needs to take up to the 1/highest_rate_input to avoid missing data  (with though thread and queue seperates between raw input and the computation). 

## Insights so far 

1. Computing the computation graph using threads or multiprocess should be done with caution and may not provide any advantage over just using simple operations with the right tools such as numpy. 




