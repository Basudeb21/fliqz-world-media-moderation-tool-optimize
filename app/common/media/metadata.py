# app/common/media/metadata.py
from __future__ import annotations
import hashlib
import mimetypes
from datetime import datetime
from app.common.media.asset import MediaAsset

class MetadataExtractor:
    """
    Extracts normalized metadata from MediaAsset.
    """
    @classmethod
    def extract(
        cls,
        media: MediaAsset,
    ) -> MediaAsset:
        """
        Populate media.metadata.
        """
        stat = media.path.stat()
        media.metadata.update(
            {
                "filename": media.path.name,
                "extension": media.path.suffix.lower(),
                "mime_type": media.mime_type
                or mimetypes.guess_type(media.path)[0],
                "size_bytes": stat.st_size,
                "created_at": datetime.fromtimestamp(
                    stat.st_ctime
                ),
                "modified_at": datetime.fromtimestamp(
                    stat.st_mtime
                ),
                "sha256": cls.sha256(media),
            }
        )
        return media

    @staticmethod
    def sha256(
        media: MediaAsset,
        chunk_size: int = 1024 * 1024,
    ) -> str:
        """
        Calculate SHA-256 hash.
        """
        hasher = hashlib.sha256()
        with open(media.path, "rb") as file:
            while chunk := file.read(chunk_size):
                hasher.update(chunk)
        return hasher.hexdigest()