# MISLEADING-DATA-DETECTOR
ai-data-integrity-auditor/
│
├── README.md
├── checklist.md
├── requirements.txt
├── pyproject.toml
├── .env.example
├── .gitignore
│
├── data/
│   ├── raw/                 # Original input datasets
│   ├── processed/           # Cleaned / transformed data
│   ├── reference/           # Historical / baseline distributions
│   └── samples/             # Test datasets
│
├── src/
│   ├── ingestion/           # Phase 1
│   │   ├── loader.py
│   │   ├── schema_validator.py
│   │   └── metadata_extractor.py
│   │
│   ├── profiling/           # Phase 2
│   │   ├── missing_values.py
│   │   ├── outliers.py
│   │   ├── cardinality.py
│   │   └── health_report.py
│   │
│   ├── distribution/        # Phase 3
│   │   ├── subgroup_analysis.py
│   │   ├── psi.py
│   │   ├── kl_divergence.py
│   │   └── representation_report.py
│   │
│   ├── bias/                # Phase 4
│   │   ├── sensitive_features.py
│   │   ├── disparity_metrics.py
│   │   ├── proxy_detection.py
│   │   └── bias_report.py
│   │
│   ├── fallacies/           # Phase 5
│   │   ├── simpsons_paradox.py
│   │   ├── spurious_corr.py
│   │   ├── confounding.py
│   │   └── fallacy_report.py
│   │
│   ├── temporal/            # Phase 6
│   │   ├── leakage_detection.py
│   │   ├── drift_detection.py
│   │   ├── feature_timeline.py
│   │   └── temporal_report.py
│   │
│   ├── scoring/
│   │   ├── trust_score.py
│   │   └── risk_aggregation.py
│   │
│   ├── explanations/
│   │   └── plain_english.py
│   │
│   ├── api/
│   │   ├── main.py           # FastAPI entry
│   │   ├── routes.py
│   │   └── schemas.py
│   │
│   ├── utils/
│   │   ├── config.py
│   │   ├── logger.py
│   │   └── helpers.py
│   │
│   └── __init__.py
│
├── reports/
│   ├── json/
│   └── pdf/
│
├── tests/
│   ├── test_ingestion.py
│   ├── test_profiling.py
│   ├── test_distribution.py
│   ├── test_bias.py
│   ├── test_fallacies.py
│   └── test_temporal.py
│
├── docker/
│   ├── Dockerfile
│   └── docker-compose.yml
│
└── scripts/
    ├── run_pipeline.py
    └── generate_report.py
