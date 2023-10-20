# 練習

1. 請為 Nginx/API/Redis 加上對應的 liveness 探針
    - Nginx 請使用 httpGet 方式
    - API 請使用 tcpSocket 方式
    - Redis 請使用 exec 方式 (可以使用下面指令確認 Redis 是否存活)
        - redis-cli set "KEY" "VALUE"

2. 請為 Nginx/API 加上對應的 HPA
    - 要使用 HPA 的話，Pod 需要做 resources.requests 設定
    - 當 CPU 平均使用率達 30% 時進行擴展
    - 可以不用管 scaling behavior

3. 請加上 Affinity & Anti-Affinity

    - 讓 Nginx Pod 之間盡量分在不同節點
    - 讓 API Pod 之間盡量分在不同節點
    - 讓 Nginx 與 API 的 Pod 兩者盡量在同一個節點
    - `topologyKey` 請使用 `kubernetes.io/hostname`

4. Ingress

請修改下面 Ingress YAML，將流量導入到 `nginx-svc`

```yaml
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: foobar-ingress
  namespace: <namespace>
spec:
  ingressClassName: nginx
  rules:
  - http:
      paths:
      - path: /<user-id>
        pathType: Prefix
        backend:
          service:
            name: nginx-svc
            port:
              number: 80
```

部署後應該會發現 Ingress 回傳 Error HTTP Code，請猜測原因?
如知道原因，請嘗試修正他

5. Taints & Toleration

請講師將其中一台節點設定以下 taints

```bash
kubectl taint nodes <node> <key>=<value>:<taint-effect>

# Example
kubectl taint nodes <node> ghost=house:PreferNoSchedule
```

請為 Redis Toleration 加上對應的 Toleration，讓 Redis Pod 能跑在該節點上