import platform, socket, re, uuid, json, psutil, logging
from multiprocessing import Process


# store system information
system_information = {}


# gather system information
def get_sysinfo():
    try:
        # temporary storage array
        info = {}
        # get: universal unique identifier for the device
        info['uuid'] = str(uuid.uuid4())
        # get: operating system platform
        info['platform'] = platform.system()
        # get: operating system release information
        info['platform-release'] = platform.release()
        # get: operating system version
        info['platform-version'] = platform.version()
        # get: sysem architecture version, example: x64
        info['architecture'] = platform.machine()
        # get: hostname
        info['hostname'] = socket.gethostname()
        # get: ip address of the user
        info['ip-address'] = socket.gethostbyname(socket.gethostname())
        # get: mac address of the user
        info['mac-address'] = ':'.join(re.findall('..', '%012x' % uuid.getnode()))
        # get: processer information
        info['processor'] = platform.processor()
        # get: ram in gigabytes
        info['ram'] = str(round(psutil.virtual_memory().total / (1024.0 **3)))+" GB"
        # return the array as json dump
        return json.dumps(info)
    except Exception as e:
        pass


# start and save telemetry information
def get_information():
    # get the json dump telemetry from get_sysinfo() function
    system_information = json.loads(get_sysinfo())
    try:
        # save the information as json
        out_file = open('../appdata/telemetry.json','w+')
        # dump the information in json file with beautification
        json.dump(system_information, out_file, indent=4)
    except Exception as e:
        pass


# run as a parallel process
def parallel_runner():
    # define a parallel process with get_information() function as target
    process_sysinfo = Process(target=get_information)
    process_sysinfo.start() # start the parallel process
    process_sysinfo.join() # join the parallel process


# requireed for multiprocessing
if __name__ == "__main__":
    parallel_runner() # start parallel_runner() function
