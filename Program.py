from TransLoader import TransLoader
import logging
_logger = logging.getLogger(__name__)

if __name__ == '__main__':

    logging.basicConfig(
         level=logging.INFO,
         format= '[%(asctime)s] {%(pathname)s:%(lineno)d} %(levelname)s - %(message)s',
         datefmt='%H:%M:%S'
     )

    trans_loader = TransLoader()

    print 'CyberMars charge'
    trans_list = trans_loader.load_charge_file('charge/test.char')
    for trans in trans_list:
        print trans.to_string()

    print 'csv charge'
    trans_list = trans_loader.load_charge_file('charge/test.csv')
    for trans in trans_list:
        print trans.to_string()

    print 'json charge'
    trans_list = trans_loader.load_charge_file('charge/test.json')
    for trans in trans_list:
        print trans.to_string()
