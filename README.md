<p align="center">
  <img src="assets/mark.svg" width="76" alt="">
</p>

<h1 align="center">hey, i'm shubham</h1>

<p align="center">
  systems &amp; backend engineer from jaipur, india — i also go by <b>kira</b>.<br>
  i build inference infrastructure, low-level tools, and production paths that stay understandable under load.
</p>

<p align="center">
  <a href="https://github.com/bas3line" title="github"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/icons/github-dark.svg"><img src="assets/icons/github.svg" width="22" alt="github"></picture></a>
  &nbsp;&nbsp;
  <a href="https://x.com/inlovewithgo" title="x"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/icons/x-dark.svg"><img src="assets/icons/x.svg" width="22" alt="x"></picture></a>
  &nbsp;&nbsp;
  <a href="https://www.linkedin.com/in/extractings/" title="linkedin"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/icons/linkedin-dark.svg"><img src="assets/icons/linkedin.svg" width="22" alt="linkedin"></picture></a>
  &nbsp;&nbsp;
  <a href="mailto:hi@yshubham.com" title="hi@yshubham.com"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/icons/mail-dark.svg"><img src="assets/icons/mail.svg" width="22" alt="email"></picture></a>
  &nbsp;&nbsp;
  <a href="https://cal.com/shubhamyadav" title="book a call"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/icons/calendar-dark.svg"><img src="assets/icons/calendar.svg" width="22" alt="book a call"></picture></a>
</p>

<p align="center">
  <a href="https://yshubham.com"><img src="assets/mark.svg" width="13" alt=""> website</a> ·
  <a href="https://yshubham.com/work/"><img src="assets/mark.svg" width="13" alt=""> work</a> ·
  <a href="https://yshubham.com/blog/"><img src="assets/mark.svg" width="13" alt=""> writing</a> ·
  <a href="https://yshubham.com/tools/"><img src="assets/mark.svg" width="13" alt=""> tools</a> ·
  <a href="https://git.yshubham.com/"><img src="assets/favicons/git.svg" width="13" alt=""> git</a> ·
  <a href="https://yshubham.com/manga/"><img src="assets/mark.svg" width="13" alt=""> shelf</a> ·
  <a href="https://yshubham.com/shubham.json"><img src="assets/mark.svg" width="13" alt=""> shubham.json</a>
</p>

---

## work

**software engineer** at **[commandcode.ai](https://commandcode.ai)** · jun 2026 — present

inference infrastructure and devops for production ai systems — high-throughput apis, gpu fleet reliability, deployments, observability, and safe release paths.

previously:

| | role | what i did |
|---|---|---|
| **[routing.run](https://routing.run)** | co-founder & cto | built an llm api gateway from scratch — multi-provider routing, fallback, auth, billing, provider health. ran it through acquisition and handover. |
| **[MegaLLM](https://megallm.io)** | founding member & senior software engineer | a swift macos app with system-level integrations, a multi-tenant reseller platform, go and typescript routing backends, lora training workflows, jenkins release pipelines. |
| **[DynTech](https://enigma.ws)** | software engineer | auth and subscription systems for a copy-trading platform, plus the jenkins/docker deployment path. |
| **[Groot Music](https://grootbot.pro)** | software engineer | scaled the backend of a high-traffic discord music bot across thousands of servers. |
| **MemePay** | cto | a solana trading product across frontend, backend, and deployment. |
| **Meds Reminder** | backend developer | apis and data handling for medication reminders and scheduling. |

the full timeline lives at **[yshubham.com/work](https://yshubham.com/work/)**.

## projects

### [routing.run](https://routing.run) · llm api gateway

a stable openai-compatible endpoint over a model market that changes every week. multi-provider routing, fallback, authentication, billing, and provider health monitoring. built it, ran it in production, handed it over at acquisition.
<br><sub>python · fastapi · postgresql · redis · docker — [case study](https://yshubham.com/work/routing-run/)</sub>

### [Sandbox](https://github.com/bas3line/sandbox) · disposable environments

coding environments for humans and agents that expire, with policy enforced by the server instead of the prompt. risk-aware scheduling, docker workers, a typed remote cli, and mcp + skills for agents.
<br><sub>rust · postgresql · nats · docker · mcp — [docs](https://docs.yshubham.com/v2/products/sandbox)</sub>

### [Watchman](https://github.com/bas3line/watchman) · gpu inference operations

an operator's lens for gpu inference servers: inspect them, benchmark them, and catch trouble before users do. monitoring, debugging, and safe operation of production inference infrastructure.
<br><sub>rust — [docs](https://docs.yshubham.com/v2/products/watchman)</sub>

### [UltraBalancer](https://github.com/bas3line/ultrabalancer) · http/2 load balancer

a small, inspectable data path built to stay fast when connection counts stop being friendly.
<br><sub>rust · tokio · http/2 · prometheus — [case study](https://yshubham.com/work/ultrabalancer/)</sub>

### [Context Bridge](https://github.com/bas3line/Context-Bridge) · agent session handoffs

moves useful coding-session context between opencode, claude code, and codex without pretending hidden model state is portable. local canonical event log, git-state checks, strict redaction.
<br><sub>rust — [docs](https://docs.yshubham.com/v2/context-bridge/overview)</sub>

### [Honeypot](https://github.com/bas3line/honeypot) · ssh honeypot

an ssh honeypot for cybersecurity training and attack-surface observation.
<br><sub>rust</sub>

## things i run

self-hosted, and public if you want to poke at them:

- **[git.yshubham.com](https://git.yshubham.com/)** — forgejo mirror of my repos, resynced every two minutes
- **[docs.yshubham.com](https://docs.yshubham.com)** — tool docs, agent skills, and mcp setup
- **[status.yshubham.com](https://status.yshubham.com)** — live health checks and incident notes
- **[trace.yshubham.com](https://trace.yshubham.com)** — browser-side https endpoint probe and request-path map
- **[objects.yshubham.com](https://objects.yshubham.com/)** — screened, expiring public object storage on r2 + queues

## outside code

i read and collect manga, manhwa, comics, and novels.

currently on the shelf: **Bakuman** (15/20), **Kagurabachi** (all 7 english volumes), and **Bleach** (9/74). also working through **Dandadan**, **Sakamoto Days**, **Fullmetal Alchemist**, and **Alice in Borderland** — with complete runs of **Naruto**, **Death Note**, **Solo Leveling**, **The Boys**, and **Invincible** already done.

the whole collection is at **[yshubham.com/manga](https://yshubham.com/manga/)**.

## skills

**languages**

<p>
  <img src="assets/tech/go.svg" width="30" title="Go" alt="Go">&nbsp;
  <picture><source media="(prefers-color-scheme: dark)" srcset="assets/tech/rust-dark.svg"><img src="assets/tech/rust.svg" width="30" title="Rust" alt="Rust"></picture>&nbsp;
  <img src="assets/tech/python.svg" width="30" title="Python" alt="Python">&nbsp;
  <img src="assets/tech/typescript.svg" width="30" title="TypeScript" alt="TypeScript">&nbsp;
  <img src="assets/tech/c.svg" width="30" title="C" alt="C">&nbsp;
  <img src="assets/tech/cplusplus.svg" width="30" title="C++" alt="C++">&nbsp;
  <img src="assets/tech/zig.svg" width="30" title="Zig" alt="Zig">&nbsp;
  <img src="assets/tech/swift.svg" width="30" title="Swift" alt="Swift">&nbsp;
  <img src="assets/tech/nodejs.svg" width="30" title="Node.js" alt="Node.js">&nbsp;
  <picture><source media="(prefers-color-scheme: dark)" srcset="assets/tech/bun-dark.svg"><img src="assets/tech/bun.svg" width="30" title="Bun" alt="Bun"></picture>
</p>

**inference &amp; gpu**

<p>
  <img src="assets/tech/nvidia.svg" width="30" title="NVIDIA CUDA" alt="CUDA">&nbsp;
  <img src="assets/tech/vllm.svg" width="30" title="vLLM" alt="vLLM">&nbsp;
  <img src="assets/tech/pytorch.svg" width="30" title="PyTorch" alt="PyTorch">&nbsp;
  <img src="assets/tech/huggingface.svg" width="30" title="Transformers" alt="Transformers">
</p>

**data**

<p>
  <img src="assets/tech/postgresql.svg" width="30" title="PostgreSQL" alt="PostgreSQL">&nbsp;
  <img src="assets/tech/redis.svg" width="30" title="Redis" alt="Redis">&nbsp;
  <img src="assets/tech/valkey.png" width="30" title="Valkey" alt="Valkey">&nbsp;
  <picture><source media="(prefers-color-scheme: dark)" srcset="assets/tech/sqlite-dark.svg"><img src="assets/tech/sqlite.svg" width="30" title="SQLite" alt="SQLite"></picture>&nbsp;
  <img src="assets/tech/clickhouse.svg" width="30" title="ClickHouse" alt="ClickHouse">&nbsp;
  <img src="assets/tech/scylladb.svg" width="30" title="ScyllaDB" alt="ScyllaDB">
</p>

**messaging**

<p>
  <img src="assets/tech/nats.svg" width="30" title="NATS" alt="NATS">&nbsp;
  <picture><source media="(prefers-color-scheme: dark)" srcset="assets/tech/kafka-dark.svg"><img src="assets/tech/kafka.svg" width="30" title="Apache Kafka" alt="Kafka"></picture>&nbsp;
  <img src="assets/tech/rabbitmq.svg" width="30" title="RabbitMQ" alt="RabbitMQ">
</p>

**containers &amp; orchestration**

<p>
  <img src="assets/tech/docker.svg" width="30" title="Docker" alt="Docker">&nbsp;
  <img src="assets/tech/kubernetes.svg" width="30" title="Kubernetes" alt="Kubernetes">&nbsp;
  <picture><source media="(prefers-color-scheme: dark)" srcset="assets/tech/helm-dark.svg"><img src="assets/tech/helm.svg" width="30" title="Helm" alt="Helm"></picture>&nbsp;
  <img src="assets/tech/argo.svg" width="30" title="Argo CD" alt="Argo CD">&nbsp;
  <img src="assets/tech/istio.svg" width="30" title="Istio" alt="Istio">
</p>

**ci/cd &amp; configuration**

<p>
  <img src="assets/tech/jenkins.svg" width="30" title="Jenkins" alt="Jenkins">&nbsp;
  <img src="assets/tech/github-actions.svg" width="30" title="GitHub Actions" alt="GitHub Actions">&nbsp;
  <img src="assets/tech/gitlab.svg" width="30" title="GitLab CI/CD" alt="GitLab CI/CD">&nbsp;
  <img src="assets/tech/ansible.svg" width="30" title="Ansible" alt="Ansible">&nbsp;
  <img src="assets/tech/terraform.svg" width="30" title="Terraform" alt="Terraform">&nbsp;
  <img src="assets/tech/vault.svg" width="30" title="HashiCorp Vault" alt="Vault">
</p>

**edge &amp; proxies**

<p>
  <img src="assets/tech/nginx.svg" width="30" title="Nginx" alt="Nginx">&nbsp;
  <img src="assets/tech/traefik.svg" width="30" title="Traefik" alt="Traefik">&nbsp;
  <img src="assets/tech/caddy.svg" width="30" title="Caddy" alt="Caddy">
</p>

**observability**

<p>
  <img src="assets/tech/grafana.svg" width="30" title="Grafana" alt="Grafana">&nbsp;
  <img src="assets/tech/prometheus.svg" width="30" title="Prometheus" alt="Prometheus">&nbsp;
  <picture><source media="(prefers-color-scheme: dark)" srcset="assets/tech/opentelemetry-dark.svg"><img src="assets/tech/opentelemetry.svg" width="30" title="OpenTelemetry" alt="OpenTelemetry"></picture>&nbsp;
  <picture><source media="(prefers-color-scheme: dark)" srcset="assets/tech/sentry-dark.svg"><img src="assets/tech/sentry.svg" width="30" title="Sentry" alt="Sentry"></picture>
</p>

**platform &amp; tools**

<p>
  <img src="assets/tech/aws.svg" width="30" title="AWS" alt="AWS">&nbsp;
  <img src="assets/tech/cloudflare.svg" width="30" title="Cloudflare" alt="Cloudflare">&nbsp;
  <picture><source media="(prefers-color-scheme: dark)" srcset="assets/tech/linux-dark.svg"><img src="assets/tech/linux.svg" width="30" title="Linux" alt="Linux"></picture>&nbsp;
  <img src="assets/tech/git.svg" width="30" title="Git" alt="Git">&nbsp;
  <img src="assets/tech/neovim.svg" width="30" title="Neovim" alt="Neovim">&nbsp;
  <img src="assets/tech/astro.svg" width="30" title="Astro" alt="Astro">
</p>

<p align="center">
  <sub>icons vendored from <a href="https://yshubham.com">yshubham.com</a> · <a href="mailto:hi@yshubham.com">hi@yshubham.com</a></sub>
</p>
