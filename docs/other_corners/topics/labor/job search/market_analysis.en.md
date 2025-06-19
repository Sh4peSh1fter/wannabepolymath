# Market Analysis

## Job Applications

list all the available jobs that you are seeking and from which you will pull all the data from, so we have a reference.  
we can add a column of the seniority / title itself just for easier reading.

## Job Experience Table

list all the titles that are wanted as job experience and the minimum years of it. 

| Job Title                 | + (no years mentioned)    | +2    | +3    | +4    | +5    | +6    | +10   |
| ------------------------- | ------------------------- | ----- | ----- | ----- | ----- | ----- | ----- |
| DevOps                    | 1                         | 2     | 6     | 3     | 4     | 0     | 0     |
| Production Engineer       | 0                         | 2     | 1     | 0     | 1     | 0     | 0     |
| Infrastructure Engineer   | 0                         | 0     | 2     | 0     | 0     | 0     | 0     |
| Platform Engineer         | 0                         | 1     | 5     | 2     | 4     | 0     | 0     |
| SRE                       | 0                         | 1     | 4     | 0     | 2     | 0     | 0     |

## Tools Table

list all the topics and tools that are required for the job.  
not always we know all the tools that are wanted and used. so just go application by application and add the tools as you see them.  
dividing them to topics is more readable but you can also have just a tools column.

| Topic                     | Tools         | +     | +2    | +3    | +4    | +5    | +6    | +10   |
| ------------------------- | ------------- | ----- | ----- | ----- | ----- | ----- | ----- | ----- |
| IaC                       | terraform     | 2     | 6     | 3     | 4     | 0     | 0     | 0     |
|                           | pulumi        | 2     | 1     | 0     | 1     | 0     | 0     | 0     |
|                           | crossplane    | 0     | 2     | 0     | 0     | 0     | 0     | 0     |
| Configuration Management  | ansible       | 1     | 5     | 2     | 4     | 0     | 0     | 0     |
|                           | chef          | 2     | 1     | 0     | 1     | 0     | 0     | 0     |
|                           | puppet        | 0     | 2     | 0     | 0     | 0     | 0     | 0     |
| CI CD                     | gh actions    | 1     | 5     | 2     | 4     | 0     | 0     | 0     |
|                           | gitlab ci     | 2     | 1     | 0     | 1     | 0     | 0     | 0     |


## end

after writing everything down to the tables, we can visualize the relevancy of each component in the table with a heat map.  
automatically color all the cells based on value.