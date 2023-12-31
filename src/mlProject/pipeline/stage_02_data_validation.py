from typing import Any
from mlProject.config.configuration import ConfigurationManager
from mlProject.components.data_validation import DataValidation
from mlProject import logger



class DataValidationTrainingPipeline:
    def __init__(self, cfg_manager) -> None:
        self.cfg_manager = cfg_manager
    
    def main(self) -> Any:
        data_validation_config = self.cfg_manager.get_data_validation_config()
        data_validation = DataValidation(data_validation_config)
        return data_validation.validate_all_columns()

if __name__ == "__main__":
    try:
        cfg_manager = ConfigurationManager()
        STAGE_NAME = "Data Validation"
        logger.info(f">>>>>>>>>>>>>> stage {STAGE_NAME} started <<<<<<<<<<<<<<")
        DataValidationTrainingPipeline(cfg_manager).main()
        logger.info(f">>>>>>>>>>>>>> stage {STAGE_NAME} completed <<<<<<<<<<<<<<")
    except Exception as e:
        logger.exception(e)
        raise e