# Python REST API Sample

## 打包鏡像

```bash
docker build -t <registry>/workshop/<image-name>:<image-tag> ./python-app

# Example
docker build -t registry.srcmesh.dev/workshop/foobar:0.0.1 ./python-app
```

## 推送鏡像

```bash
echo <password> | docker login -u <username> --password-stdin <registry>

docker push image <registry>/workshop/<image-name>:<image-tag>
```

## 確定能拉取鏡像

```bash
# remove local image
docker rm <registry>/workshop/<image-name>:<image-tag>

# pull image from remote registry
docker pull <registry>/workshop/<image-name>:<image-tag>
```