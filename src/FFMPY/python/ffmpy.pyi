

from dataclasses import dataclass
from typing import Any, Optional, List, Dict, Union
import numpy as np
import torch

@dataclass
class ReaderConfig:
    as_numpy: bool = False # If True, returns frames as NumPy array, else as torch.Tensor
    dtype: str = "uint8"
    to_cpu: bool = False
    
    def __post_init__(self):
        if self.dtype not in ["uint8", "float", "half"]:
            raise ValueError(f"Invalid dtype: {self.dtype}")
        if self.as_numpy:
            self.to_cpu = True
            
class VideoReader:
    def __init__(self, input_video : str, config: Optional[ReaderConfig] = None):
        self.input_video = input_video
        self.config = ReaderConfig() if config is None else config

    def readFrame(self) -> Union[torch.Tensor, np.ndarray, None]:
        """
        Read and return the next video frame.

        :return: A video frame as a Frame object, a PyTorch tensor, a NumPy array, or None if no frame is read.
        """
        ...

    def seek(self, frame_number: int) -> None:
        """
        Seek to a specific frame number in the video.

        :param frame_number: The frame number to seek to.
        """
        ...

    def supportedCodecs(self) -> List[str]:
        """
        Get a list of supported codecs.

        :return: A list of codec names.
        """
        ...
    
    def getProperties(self) -> Dict[str, Union[int, float]]:
        """
        Get properties of the video.

        :return: A dictionary containing video properties (e.g., width, height, fps, duration, totalframes, pixelFormat).
        """
        ...

    def __len__(self) -> int:
        """
        Get the total number of frames in the video.

        :return: Total frame count.
        """
        ...

    def __iter__(self) -> 'VideoReader':
        """
        Return the iterator object itself.

        :return: The VideoReader instance.
        """
        ...

    def __next__(self) -> Union[torch.Tensor, np.ndarray]:
        """
        Return the next frame in the video.

        :return: The next video frame as a Frame object, a PyTorch tensor, or a NumPy array.
        :raises StopIteration: When there are no more frames.
        """
        ...

    def __enter__(self) -> 'VideoReader':
        """
        Enter the runtime context related to the VideoReader object.

        :return: The VideoReader instance.
        """
        ...

    def __exit__(
        self, 
        exc_type: Optional[type], 
        exc_value: Optional[BaseException], 
        traceback: Optional[Any]
    ) -> bool:
        """
        Exit the runtime context and handle exceptions.

        :param exc_type: Exception type.
        :param exc_value: Exception value.
        :param traceback: Traceback object.
        :return: False to indicate that exceptions should not be suppressed.
        """
        ...
