from build_failure_predictor import predict_failure

predict_failure(
    changed_files=6,
    previous_failures=2,
    build_duration=75
)