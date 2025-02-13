import sys

def error_message_details(error, error_detail:sys):
    _,_,exc_tb=error_detail.exc_info()    #error_detail is from the sys. so basically it has three details and in those we just need a last one of the detail
    file_name=exc_tb.tb_frame.f_code.co_filename
    error_message="Error has occured in the python script [{0}] line number [{1}] error message [{2}]".format(
        file_name, exc_tb.tb_lineno, str(error)
        )
    return error_message

class CustomException(Exception):
    def __init__(self, error_message, error_detail:sys):
        super().__init__(error_message)
        self.error_message=error_message_details(error_message, error_detail=error_detail)

    def __str__(self):
        return self.error_message