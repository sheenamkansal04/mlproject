import sys


def error_message_detail(error, error_detail:sys):
    exc_type, exc_value, exc_traceback = error_detail.exc_info()
    file_name = exc_traceback.tb_frame.f_code.co_filename
    line_number = exc_traceback.tb_lineno
    function_name  = exc.traceback.tb_frame.f_code.co_name
    error_message = f"Error occured in script : {file_name} line number : {line_number} function name : {function_name} error message : {error}"

    return error_message

class CustomException(Exception):

    def __init__(self, error_message,error_detail:sys):
        super().__init__(error_message)
        self.error_message = error_message_detail(error_message, error_detail = error_detail)

    def __str__(self):
        return self.error_message


if __name__ == "__main__":
    try:
        a= 1/0
    except Exception as e:
        logging.info("Error occured in logger file")
        raise CustomException(e,sys)