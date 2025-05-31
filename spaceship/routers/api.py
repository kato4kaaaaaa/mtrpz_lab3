from fastapi import APIRouter

router = APIRouter()


@router.get("/matrix_multiply")
def matrix_multiply():
    matrix_a = np.random.randint(0, 10, size=(10, 10)).tolist()
    matrix_b = np.random.randint(0, 10, size=(10, 10)).tolist()
    product = (np.array(matrix_a) @ np.array(matrix_b)).tolist()

    return {
        "matrix_a": matrix_a,
        "matrix_b": matrix_b,
        "product": product,
    }

