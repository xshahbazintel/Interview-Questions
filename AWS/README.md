what are inline and managed policies, major differences?
An AWS managed policy is a standalone policy that is created and administered by AWS.
You cannot change the permissions defined in AWS managed policies

what are endpoints in vpc?
end points are used to connect other resources in aws from vpc, without routing traffic from internet.
you have gateway endpoint and interface endpoint
gateway endpoint are used for s3 and dynamodb
interface endpoint are for other aws services

gateway endpoints will have a route attached, you have to decide which route tables should have access to this endpoints
interface endpoints have sg attached, this work at subnet level

how do you redirect http traffic to https in nlb
what is nlb, why have you used it
what are sg and nacls
how do you restore snapshot of aws ebs volume in another regions
how do you connect aws instance in one region to another region without using vpc perring 
nlb vs alb
how do you deny traffic in sg?
you cant deny traffic in sg, you have to do that at nacl level
how many policies can you attach to an ec2 instance

why should you prefer private link rather than vpc peering?
let us assume a scenario in our organistion, one team has a software application running inside vpc, there are many other that uses it.
you cant do perring for all other teams vpc with your vpc, there may be a ip address overlaping and when you do vpc peering you are exposing entire vpc meaning every resources in side it, you can control it but still not desired.
vpc perring has limit of 125 connections
so you can use private link to access other vpc 
vpc private link supports only nlb or gateway load balancer


How would you design a highly available, fault-tolerant, and scalable architecture on AWS for a production workload?
Design the system to have no single point of failure. Use automated monitoring, failure detection, and failover mechanisms.

Single points of failure (SPOF) are commonly eliminated with an N+1 or 2N redundancy configuration, where N+1 is achieved via load balancing among active–active nodes, and 2N is achieved by a pair of nodes in active–standby configuration


If any of the N units fail, the spare (the "+1") can take over to maintain operation without affecting performance or service. For example, in a server setup with 3 servers (N=3), you would have 4 servers (3+1), where the 4th server is a standby that kicks in if one of the primary servers fails.

In a 2N configuration, there are exactly double the number of units needed to support the system, meaning for every essential component, there is a fully functional backup available.


