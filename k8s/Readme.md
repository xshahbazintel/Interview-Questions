Explain k8s architechture?
master/control plane components
etcd, kube-scheduler, kube-apiserver, kube-controllermanager, cloud-controllermanager
workerplane components
kubelet, kube-proxy

what is custom resource definition in k8s?
A custom resource is an object that extends the Kubernetes API or allows you to introduce your own API into a project or a cluster

what is poddisruption budget?

A PodDisruptionBudget (PDB) in Kubernetes is a resource that allows you to specify the minimum number or percentage of replicas of a pod that must be available during voluntary disruptions. This ensures that there is always a certain level of availability for your application during operations like node maintenance, pod upgrades, or scaling activities.
PodDisruptionBudget only applies to voluntary disruptions. It does not affect involuntary disruptions like node crashes or pod failures.
If a PodDisruptionBudget cannot be satisfied (e.g., if all the pods are required to be available), Kubernetes may block the disruption, such as preventing the deletion of pods during a rolling update or draining operation.

apiVersion: policy/v1
kind: PodDisruptionBudget
metadata:
  name: zk-pdb
spec:
  minAvailable: 2
  selector:
    matchLabels:
      app: zookeeper

What is Horizontal pod autoscaler?
HPA allows you to scale number of pods of a deployment based on resource utilisation metrics like cpu or memory or any other custom metrics.

write a sample deployment file for nginx?

apiVersion: apps/v1
kind: Deployment
metadata:
  name: nginx-deployment
  labels:
    app: nginx
spec:
  replicas: 3  # Number of NGINX pods to run
  selector:
    matchLabels:
      app: nginx  # Pods with this label will be managed by this deployment
  template:
    metadata:
      labels:
        app: nginx
    spec:
      containers:
        - name: nginx
          image: nginx:latest  # NGINX image from Docker Hub
          ports:
            - containerPort: 80  # Expose port 80 to access the NGINX server

kubectl create deployment nginx-deployment --image=nginx:latest --replicas=3

what is kube-scheduler, how it works?

The Kube-scheduler is a core component of Kubernetes that is responsible for selecting which node (machine) in the Kubernetes cluster should run a particular pod. Its primary task is to ensure that pods are scheduled in an efficient and optimal way based on various factors like resource availability, constraints, and other scheduling policies.

what is nodeaffinity?
Node affinity is conceptually similar to nodeSelector, allowing you to constrain which nodes your Pod can be scheduled on based on node labels.
There are two types of node affinity
requiredDuringSchedulingIgnoredDuringExecution: schedules pod only when rules are met
preferredDuringSchedulingIgnoredDuringExecution: The scheduler tries to find a node that meets the rule. If a matching node is not available, the scheduler still schedules the Pod
In the preceding types, IgnoredDuringExecution means that if the node labels change after Kubernetes schedules the Pod, the Pod continues to run.

what is persistent volume?


why do you need loadbalancer service when you have ingress controller?

how do you design ha k8s cluster



