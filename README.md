# [Sketch Blend](https://sketch-blend.isaacdev.net)

A drawing and sharing website that is powered by micro-service architecture in Kubernetes with AWS, and multiple backend languages.

![Banner](./banner.png)

### Architecture Overview

![AWS](./diagrams_image.png)

### Container Diagram

![Container Diagram](./sketch-blend-container-diagram.drawio.svg)

### Backend Services

- [API Docs](https://sketch-blend-api.isaacdev.net/docs)

  ![Swagger](https://img.shields.io/badge/-Swagger-%23Clojure?style=for-the-badge&logo=swagger&logoColor=white)

  ⚠ The Docs sometime may not be available, because the developer may shut down Kubernetes cluster to save money💵.

- [API Module Repo](https://github.com/IsaacOrzDev/sketch-blend-api-module)

  ![NodeJS](https://img.shields.io/badge/node.js-6DA55F?style=for-the-badge&logo=node.js&logoColor=white)
  ![NestJS](https://img.shields.io/badge/nestjs-%23E0234E.svg?style=for-the-badge&logo=nestjs&logoColor=white)
  ![MongoDB](https://img.shields.io/badge/MongoDB-%234ea94b.svg?style=for-the-badge&logo=mongodb&logoColor=white)

- [User Module Repo](https://github.com/IsaacOrzDev/sketch-blend-user-module)

  ![C#](https://img.shields.io/badge/c%23-%23239120.svg?style=for-the-badge&logo=c-sharp&logoColor=white)
  ![.Net](https://img.shields.io/badge/.NET-5C2D91?style=for-the-badge&logo=.net&logoColor=white)
  ![Postgres](https://img.shields.io/badge/postgres-%23316192.svg?style=for-the-badge&logo=postgresql&logoColor=white)

- [Generator Module Repo](https://github.com/IsaacOrzDev/sketch-blend-generator-module)

  ![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)

- [Document Module Repo](https://github.com/IsaacOrzDev/sketch-blend-document-module)

  ![Go](https://img.shields.io/badge/go-%2300ADD8.svg?style=for-the-badge&logo=go&logoColor=white)
  ![MongoDB](https://img.shields.io/badge/MongoDB-%234ea94b.svg?style=for-the-badge&logo=mongodb&logoColor=white)

- [Temporary API Repo](https://github.com/IsaacOrzDev/sketch-blend-temporary-api)

  ![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
  ![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)

  It is a temporary API for the frontend portal to use if the Kubernetes cluster is shut down.

### Infrastructure as Code

- [EKS / ECS Terraform Repo](https://github.com/IsaacOrzDev/sketch-blend-terraform)

  ![Terraform](https://img.shields.io/badge/terraform-%235835CC.svg?style=for-the-badge&logo=terraform&logoColor=white)
  ![AWS](https://img.shields.io/badge/AWS-%23FF9900.svg?style=for-the-badge&logo=amazon-aws&logoColor=white)
  ![Kubernetes](https://img.shields.io/badge/kubernetes-%23326ce5.svg?style=for-the-badge&logo=kubernetes&logoColor=white)
  ![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)

- [SNS / SES Email Pulumi Repo](https://github.com/IsaacOrzDev/email-service-pulumi-stack)

  ![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
  ![AWS](https://img.shields.io/badge/AWS-%23FF9900.svg?style=for-the-badge&logo=amazon-aws&logoColor=white)

- [Lambda Temporary API Pulumi Repo](https://github.com/IsaacOrzDev/sketch-blend-pulumi)

  ![TypeScript](https://img.shields.io/badge/typescript-%23007ACC.svg?style=for-the-badge&logo=typescript&logoColor=white)
  ![AWS](https://img.shields.io/badge/AWS-%23FF9900.svg?style=for-the-badge&logo=amazon-aws&logoColor=white)

### Frontend Portal

- [Portal Repo](https://github.com/IsaacOrzDev/sketch-blend-portal)

  ![Next JS](https://img.shields.io/badge/Next-black?style=for-the-badge&logo=next.js&logoColor=white)
  ![Vercel](https://img.shields.io/badge/vercel-%23000000.svg?style=for-the-badge&logo=vercel&logoColor=white)
  ![TailwindCSS](https://img.shields.io/badge/tailwindcss-%2338B2AC.svg?style=for-the-badge&logo=tailwind-css&logoColor=white)

- [Figma Design](https://www.figma.com/file/a7SYHwfehtOAOJHpDxvSQn/Sketch-Blend)

  ![Figma](https://img.shields.io/badge/figma-%23F24E1E.svg?style=for-the-badge&logo=figma&logoColor=white)
