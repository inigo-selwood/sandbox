import fastapi
import pydantic

from .. import controllers


router = fastapi.APIRouter()


class PreprocessRequest(pydantic.BaseModel):
    """
    Represents a request to preprocess text.

    Attributes
    ----------
    text: str
        The text to be processed
    """

    text: str


class PreprocessResponse(pydantic.BaseModel):
    """
    Represents the response from the text preprocessing.

    Attributes
    ----------
    tokens: list[str]
        The preprocessed text, split into tokens.
    """

    tokens: list[str]


@router.post('/preprocess')
def preprocess(request: PreprocessRequest) -> PreprocessResponse:
    """
    Endpoint to preprocess text.

    Parameters
    ----------
    request: PreprocessRequest
        The request containing the text to be preprocessed.

    Returns
    -------
    PreprocessResponse
        The response containing the preprocessed text.
    """
    result = controllers.preprocess(request.text)
    return PreprocessResponse(tokens=result)
