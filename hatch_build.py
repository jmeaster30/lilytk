from hatchling.metadata.plugin.interface import MetadataHookInterface

import lilytk

class VersionMetadataHook(MetadataHookInterface):
  def update(self, metadata):
    metadata["version"] = lilytk.__version__