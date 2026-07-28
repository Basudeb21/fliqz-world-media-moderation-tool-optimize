from app.core.redis import AttachmentState


state = AttachmentState(9999)


def test_initialize():

    assert state.initialize(
        {
            "status": "processing",
            "blocked": False,
        }
    )


def test_metadata():

    metadata = state.get_metadata()

    assert metadata["status"] == "processing"


def test_progress():

    state.update_progress(
        {
            "completed": 5,
            "total": 20,
        }
    )

    progress = state.get_progress()

    assert progress["completed"] == 5


def test_cancel():

    state.mark_cancelled()

    assert state.is_cancelled()


def test_detector():

    state.save_detector_result(

        "minor",

        {
            "confidence": 0.98,
            "detected": True,
        },

    )

    result = state.get_detector_result(
        "minor"
    )

    assert result["detected"]


def test_cleanup():

    state.delete()

    assert state.get_metadata() is None