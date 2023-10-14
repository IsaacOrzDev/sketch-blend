from diagrams import Diagram, Cluster, Edge
from diagrams.aws.storage import S3
from diagrams.aws.network import Route53, ElbApplicationLoadBalancer, VPC, PublicSubnet, PrivateSubnet, NATGateway, InternetGateway, RouteTable
from diagrams.aws.compute import Lambda, ElasticContainerService, ElasticKubernetesService, Fargate, ElasticContainerServiceService

from diagrams.aws.database import Aurora
from diagrams.aws.security import CertificateManager
from diagrams.generic.device import Tablet, Mobile
from diagrams.programming.language import Nodejs, Python, Go, Csharp
from diagrams.programming.framework import React
from diagrams.k8s import group 
from diagrams.k8s.network import Ingress, Service
from diagrams.k8s.compute import Deployment, Pod


graph_attr = {
    "fontsize": "45",
    "bgcolor": "transparent"
}

with Diagram("", graph_attr=graph_attr, show=False, direction='LR'):

    with Cluster(""):
      user_a = Tablet("Users")
      user_b = Mobile("Users")
      mongodb = Aurora("MongoDB")
      postgresql = Aurora("PostgreSQL")    

      with Cluster("Vercel"):
        portal_frontend = React("Portal")
        portal_backend = Nodejs("")
        portal_serverless = Lambda("Serverless")


      with Cluster("AWS"):

        route = Route53("Domain Names")
        cert = CertificateManager("Certificate")
        with Cluster("VPC of dev env"):
          vpc = VPC("VPC")        
          alb = ElbApplicationLoadBalancer("ALB")
          ecs = ElasticContainerService("ECS")
          fargate = Fargate("Fargate")
          service = ElasticContainerServiceService("Service")
          with Cluster("Service"):
            api_module = Nodejs("API Module")
            user_module = Csharp("User Module")
            generator_module = Python("Generator Module")
            document_module = Go("Document Module")

        ecs >> service
        ecs >> fargate
        service >> api_module
        api_module >> Edge(label="gRPC") >> user_module
        api_module >> Edge(label="gRPC") >> generator_module
        api_module >> Edge(label="gRPC") >> document_module
        document_module >> mongodb
        user_module >> postgresql

        vpc >> alb
        alb >> ecs
        route >> alb
        route >> cert >> route
        user_a >> portal_frontend
        portal_frontend >> portal_backend
        portal_frontend >> route
        portal_backend >> route

        with Cluster("VPC of prod env"):

          vpc_eks = VPC("VPC")
          public_subnets = PublicSubnet("Public Subnets")
          private_subnets = PrivateSubnet("Private Subnets")
          nat = NATGateway("NAT Gateway")
          igw = InternetGateway("Internet Gateway")
          route_table_private = RouteTable("Route Table")
          route_table_public = RouteTable("Route Table")
          alb_eks = ElbApplicationLoadBalancer("ALB")
          eks = ElasticKubernetesService("EKS")
          fargate_eks = Fargate("Fargate")
          with Cluster("K8s cluster"):
            ingress = Ingress("Ingress")
            kube_system_group = group.NS("kube_system namespace")
            application_group = group.NS("application namespace")

            alb_controller_pod = Pod("ALB Controller")
            external_dns_pod = Pod("External DNS")

            with Cluster("Public"):
              api_service = Service("API Service")
              api_deployment = Deployment("API Deployment")
              api_pod = Pod("API Pods")
              api_module_k8s = Nodejs("API Module")
            with Cluster("Private"):
              user_service = Service("User Service")
              generator_service = Service("Generator Service")
              document_service = Service("Document Service")

              user_deployment = Deployment("User Deployment")
              generator_deployment = Deployment("Generator Deployment")
              document_deployment = Deployment("Document Deployment")
              user_pod = Pod("User Pods")
              generator_pod = Pod("Generator Pods")
              document_pod = Pod("Document Pods")
              user_module_k8s = Csharp("User Module")
              generator_module_k8s = Python("Generator Module")
              document_module_k8s = Go("Document Module")              

        route >> alb_eks >> alb_controller_pod
        vpc_eks >> alb_eks
        eks >> fargate_eks
        fargate_eks >> kube_system_group
        fargate_eks >> application_group
        vpc_eks >> igw >> route_table_public
        route_table_public >> public_subnets >> nat
        nat >> route_table_private
        route_table_private >> private_subnets

        public_subnets >> alb_controller_pod >> ingress >> api_service
        private_subnets >> generator_service

        kube_system_group >> alb_controller_pod
        kube_system_group >> external_dns_pod

        application_group >> api_service
        application_group >> user_service
        application_group >> generator_service
        application_group >> document_service
        
        api_service >> api_deployment >> api_pod >> api_module_k8s
        user_service >> user_deployment >> user_pod >> user_module_k8s >> postgresql
        generator_service >> generator_deployment >> generator_pod >> generator_module_k8s
        document_service >> document_deployment >> document_pod >> document_module_k8s >> mongodb

        api_module_k8s  >> user_module_k8s
        api_module_k8s  >> generator_module_k8s
        api_module_k8s  >> document_module_k8s
              
