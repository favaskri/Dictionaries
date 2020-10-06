def check_scope():
    def do_local():
        test="local test"

    def do_non_local():
        nonlocal test
        test = "test non local"

    def do_globle():
        global test
        test="test globle"

    test="defalt"
    do_local()
    print("test value after local :"+test)
    do_non_local()
    print("test value after non local :"+test)
    do_globle()
    print("test value afer globel :"+test)

check_scope()
print("test value after main :" + test)

