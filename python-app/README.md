# Python REST API Sample

## Build Image

```bash
docker build -t <registry>/workshop/<image-name>:<image-tag> .
```

## Push Image

```bash
echo <password> | docker login -u <username> --password-stdin <registry>

docker push image <registry>/workshop/<image-name>:<image-tag>
```

## Ensure Image Exists

```bash
# remove local image
docker rm <registry>/workshop/<image-name>:<image-tag>

# pull image from remote registry
docker pull <registry>/workshop/<image-name>:<image-tag>
```