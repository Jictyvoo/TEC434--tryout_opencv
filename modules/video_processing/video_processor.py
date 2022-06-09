from os.path import join
from pathlib import Path
from typing import Callable

import cv2
from utils.generators import output_filename


class VideoProcessor:
    def __init__(self, frame_processor: Callable[[cv2.Mat], cv2.Mat]) -> None:
        self.__process_frame_callback = frame_processor

    def create_writer(
        self, original_video, filename: str, output_folder: str
    ) -> cv2.VideoWriter:
        Path(output_folder).mkdir(parents=True, exist_ok=True)
        filepath = join(output_folder, output_filename(filename))

        video_writer = cv2.VideoWriter(
            filepath + ".mp4",
            cv2.VideoWriter_fourcc(*"mp4v"),
            original_video.get(cv2.CAP_PROP_FPS),
            (
                int(original_video.get(cv2.CAP_PROP_FRAME_WIDTH)),
                int(original_video.get(cv2.CAP_PROP_FRAME_HEIGHT)),
            ),
        )
        return video_writer

    def execute(self, file_path: str, output_folder: str, debug_mode: bool = False):
        # Load the video from the file path
        video = cv2.VideoCapture(file_path)

        new_video = self.create_writer(video, file_path, output_folder)

        # Process frames
        while video.isOpened():
            # Read the next frame
            success, frame = video.read()

            # If the frame was read successfully
            if success:
                processed_frame = self.__process_frame_callback(frame)

                # Write the frame
                new_video.write(processed_frame)

                if debug_mode:
                    # Display the frame
                    cv2.imshow("Frame", processed_frame)

                    # Check if the user pressed the escape key
                    if cv2.waitKey(1) == 27:
                        break
            else:
                # If not, close the video
                video.release()
