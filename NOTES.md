** Docker notes **

--------- Docker — what every line means ------------

1. Dockerfile explained line by line

# Start from official Python image # slim = smaller size, faster to download FROM python:3.11-slim # Set working directory inside container # Like doing: cd /app WORKDIR /app # Copy requirements FIRST (caching trick) # If requirements don't change → reuse cache COPY requirements.txt . # Install dependencies inside container RUN pip install --no-cache-dir -r requirements.txt # Now copy rest of your code COPY . . # Document which port app uses EXPOSE 5000 # Command to start app when container runs CMD ["python", "app.py"]

2. Docker Compose explained

# docker compose up → start all containers # docker compose down → stop all containers # docker compose logs → see all logs # docker ps → list running containers # docker images → list all images # docker exec -it app bash → go inside container
- ports: "5000:5000" means YOUR_LAPTOP:CONTAINER. Left side is what you type in browser. Right side is what app uses inside container.
- volumes: saves data even when container stops. Without it — database is wiped every time you restart.
- depends_on: makes sure database starts before your app does.

** CI/CD notes **

-------- CI/CD — what every line means --------

CircleCI config.yml explained

# version: which CircleCI version to use version: 2.1 jobs: test: # docker: which Linux machine to run on docker: - image: cimg/python:3.11 steps: # checkout: download your code from GitHub - checkout # run: execute a shell command - run: name: Install dependencies command: pip install flask pytest - run: name: Run tests # pytest finds and runs all test files command: pytest -v # workflows: when to run which jobs workflows: main: jobs: - test # run test job on every push
- Every time you git push → CircleCI reads this file → spins up a Linux machine → runs your commands → shows ✅ or ❌

Common CI/CD commands

# Push code → triggers pipeline automatically git add . git commit -m "your message" git push # Check pipeline status on CircleCI dashboard # Green = tests passed = safe to deploy # Red = tests failed = fix before deploying

****** Kubernetes notes ********

------------ Kubernetes — what every line means -------------

deployment.yml explained

# Deployment = tells K8s how to run your app kind: Deployment spec: # replicas: how many copies to run # 2 = if one crashes, other keeps running replicas: 2 # template: what each pod looks like template: spec: containers: - name: sre-app image: python:3.11-slim # containerPort: which port app uses ports: - containerPort: 5000 # Service = gives your app a stable address kind: Service spec: # NodePort = accessible from your laptop type: NodePort

Most important kubectl commands

kubectl get pods # list all pods kubectl get nodes # list all nodes kubectl apply -f file.yml # deploy/update kubectl delete pod NAME # delete a pod kubectl logs POD_NAME # see pod logs kubectl describe pod NAME # pod details kubectl port-forward svc/NAME 8080:80 # access app
- Self healing: You deleted a pod → Kubernetes created a new one automatically. It always maintains your desired number of replicas.
- Pod vs Container: A pod is a wrapper around a container. Think of pod as the house, container as the room inside.
