what is helm?
helm is a package manager for kubernetees, that simplifies all deployment, configuration  and managing applications on kubernetes clusters
it packages kuberenetes resources into charts which are used for deployment.

what are main components of helm charts?
chart.yaml: maintains chart name, versions, description and dependencies
values.yaml: contains value for chart
templates folder: resources definition files
_helpers.tpl: holds reusable templates that can be used with other templates

how do you manage deployments/rollouts/upgrade in helm chart?
helm install <release-name> <chart-name> -f <values.yaml>
helm upgrade <release-name> <chart-name>
helm rollback <release-name> <revision-number>

what are dependencies in helm chart?
when you want to install another chart or anything before installing current chart
you can manage those in dependecies in chart.yaml


what are helm hooks?
hook allow you to do specific tasks before or after installing charts
or before or deleting chart release




