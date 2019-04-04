from refactored.preprocessing.processor.cbsr.cbsr_processor import CbsrProcessor
from refactored.preprocessing.processor.replay_attack.ra_processor import RaProcessor
from refactored.preprocessing.property.depth_extractor import DepthExtractor
from refactored.preprocessing.property.illumination_extractor import IlluminationExtractor
from refactored.preprocessing.property.original_extractor import OriginalExtractor
from refactored.preprocessing.property.saliency_extractor import SaliencyExtractor


def get_properties():
    properties = []

    saliency_extractor = SaliencyExtractor()
    illumination_extractor = IlluminationExtractor()
    depth_extractor = DepthExtractor()
    original_extractor = OriginalExtractor()

    properties.append(depth_extractor)
    properties.append(original_extractor)
    properties.append(saliency_extractor)
    properties.append(illumination_extractor)

    return properties


def make_cbsr_processor(artifacts_root):
    processor = CbsrProcessor(artifacts_root=artifacts_root,
                              dataset_name='cbsr',
                              properties=get_properties())
    return processor


def make_ra_processor(artifacts_root):
    processor = RaProcessor(artifacts_root=artifacts_root,
                            dataset_name='ra',
                            properties=get_properties())
    return processor


def make_deep_fakes_processor(artifacts_root):
    processor = DeepFakesProcessor(artifacts_root=artifacts_root,
                            dataset_name='deep_fakes',
                            properties=get_properties())
    return processor
