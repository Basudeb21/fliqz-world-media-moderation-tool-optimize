FliqzWorld AI Moderation Engine Development Roadmap (v1.0)
Phase 0 — Foundation ✅ (Completed)

This phase gives us the infrastructure every other module depends on.

Configuration
    ✅ Settings
    ✅ Config Loader
    ✅ Config Validator
    ✅ Config Manager

Logging
    ✅ Structured Logger

Metrics
    ✅ Prometheus Registry

Redis
    ✅ Client
    ✅ Service
    ✅ Keys
    ✅ Serializer
    ✅ AttachmentState

Status:

Phase 0
████████████████████ 100%
Phase 1 — Contracts

This defines the language every service speaks.

contracts/

□ chunk_job.py
□ detector_result.py
□ aggregation_result.py
□ upload_request.py
□ worker_registration.py
□ heartbeat.py
□ report.py
□ evidence.py

After this phase:

Coordinator knows what to produce.
Scheduler knows what to send.
Workers know what to receive.
Aggregator knows what to merge.

Status

Phase 1
□□□□□□□□□□ 0%
Phase 2 — Redis Infrastructure

Current

Redis

Still remaining

□ Streams
□ Distributed Locks
□ Pub/Sub
□ Retry
□ Heartbeat

After this phase

Every service can communicate.

Phase 3 — Storage Layer
storage/

□ StorageManager
□ Local Storage
□ MinIO Adapter
□ S3 Adapter

□ Evidence Storage
□ Report Storage
□ Frame Storage
Phase 4 — Upload Coordinator

The entry point of the moderation engine.

□ Upload API

□ Upload Coordinator

□ File Validation

□ MIME Detection

□ Metadata Extraction

□ Image Pipeline

□ Video Pipeline Router

At this point we can successfully accept uploads.

Phase 5 — Video Pipeline
□ Frame Extractor

□ Chunk Generator

□ Manifest Creator

□ Temporary Storage

□ Cleanup Hooks

Input

video.mp4

Output

chunk_001

chunk_002

chunk_003
Phase 6 — Scheduler

This is the brain.

□ Worker Registry

□ Detector Registry

□ Queue Manager

□ Job Assigner

□ Priority Queue

□ Dynamic Scheduling

□ Cancellation
Phase 7 — Worker Framework

Generic worker implementation.

□ Base Worker

□ GPU Manager

□ Worker Lifecycle

□ Error Handling

□ Retry Logic

□ Metrics

□ Health Check

After this

Building a detector becomes easy.

Phase 8 — Detector Framework

This is huge.

We build

BaseDetector

Then every detector becomes

MinorDetector

WeaponDetector

NSFWDetector

PIIDetector

...

using exactly the same interface.

Phase 9 — First Detector (Minor)

Only one detector.

Completely production-ready.

□ YOLO

□ Face

□ Age

□ Voting

□ Evidence

□ Result

Once Minor works...

Every remaining detector is mostly plug-and-play.

Phase 10 — Aggregator
□ Merge Results

□ Final Decision

□ Policy Engine

□ JSON Report

□ Database Event
Phase 11 — Database
□ SQLAlchemy Models

□ Repository

□ Database Writer

□ Transactions
Phase 12 — Policies

Your architecture supports multiple platforms.

We'll implement

OnlyFans

Fansly

Instagram

TikTok

Reddit

Custom

Each platform has different moderation rules.

Phase 13 — Monitoring
□ Prometheus

□ Grafana

□ Dashboard

□ Queue Length

□ GPU Usage

□ FPS

□ Detector Time
Phase 14 — Deployment
□ Docker

□ Docker Compose

□ Kubernetes

□ GPU Scaling

□ Production Config
Phase 15 — Performance
□ Batch Processing

□ TensorRT

□ ONNX

□ GPU Optimization

□ Async Processing
Overall Progress
████████████████████████████████████████████████

Phase 0  Foundation            ████████████████████ 100%

Phase 1  Contracts             ░░░░░░░░░░░░░░░░░░░░   0%

Phase 2  Redis                 ░░░░░░░░░░░░░░░░░░░░   0%

Phase 3  Storage               ░░░░░░░░░░░░░░░░░░░░   0%

Phase 4  Upload Coordinator    ░░░░░░░░░░░░░░░░░░░░   0%

Phase 5  Video Pipeline        ░░░░░░░░░░░░░░░░░░░░   0%

Phase 6  Scheduler             ░░░░░░░░░░░░░░░░░░░░   0%

Phase 7  Worker Framework      ░░░░░░░░░░░░░░░░░░░░   0%

Phase 8  Detector Framework    ░░░░░░░░░░░░░░░░░░░░   0%

Phase 9  Minor Detector        ░░░░░░░░░░░░░░░░░░░░   0%

Phase 10 Aggregator            ░░░░░░░░░░░░░░░░░░░░   0%

Phase 11 Database              ░░░░░░░░░░░░░░░░░░░░   0%

Phase 12 Policies              ░░░░░░░░░░░░░░░░░░░░   0%

Phase 13 Monitoring            ░░░░░░░░░░░░░░░░░░░░   0%

Phase 14 Deployment            ░░░░░░░░░░░░░░░░░░░░   0%

Phase 15 Performance           ░░░░░░░░░░░░░░░░░░░░   0%