import time
import conf
import reserve


def main():
    conf.get_info()
    for i in range(conf.retry_times):
        print("第" + str(i+1) + "次尝试")
        if reserve.reserve():
            exit()
        time.sleep(conf.interval)
    print("预定失败")


if __name__ == '__main__':
    main()
