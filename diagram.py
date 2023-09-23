from diagrams import Diagram, Cluster, Edge
from diagrams.aws.storage import S3
from diagrams.aws.network import Route53, ElbApplicationLoadBalancer
from diagrams.aws.compute import Lambda, ElasticContainerService, Fargate, ElasticContainerServiceService
from diagrams.aws.database import Aurora
from diagrams.aws.security import CertificateManager
from diagrams.generic.device import Tablet, Mobile
from diagrams.programming.language import Nodejs, Python, Go, Csharp
from diagrams.programming.framework import React

graph_attr = {
    "fontsize": "45",
    "bgcolor": "transparent"
}

with Diagram("", graph_attr=graph_attr, show=False, direction='LR'):
    with Cluster(""):
      user_a = Tablet("Users")
      user_b = Mobile("Users")

      with Cluster("Vercel"):
        portal_frontend = React("Portal")
        portal_backend = Nodejs("")
        portal_serverless = Lambda("Serverless")


      with Cluster("AWS"):

        route = Route53("Domain Name")
        cert = CertificateManager("Certificate")
        alb = ElbApplicationLoadBalancer("ALB")
        with Cluster("Cluster"):
          ecs = ElasticContainerService("ECS")
          fargate = Fargate("Fargate")
          service = ElasticContainerServiceService("Service")
        with Cluster("Service"):
          api_module = Nodejs("API Module")
          user_module = Csharp("User Module")
          generator_module = Python("Generator Module")
          document_module = Go("Document Module")
        
      mongodb = Aurora("MongoDB")
      postgresql = Aurora("PostgreSQL")

    ecs >> service
    service >> api_module
    api_module >> Edge(label="gRPC") >> user_module
    api_module >> Edge(label="gRPC") >> generator_module
    api_module >> Edge(label="gRPC") >> document_module
    document_module >> mongodb
    user_module >> postgresql

    alb >> ecs
    route >> alb
    route >> cert >> route
    user_a >> portal_frontend
    portal_frontend >> portal_backend
    portal_frontend >> route
    portal_backend >> route
              
