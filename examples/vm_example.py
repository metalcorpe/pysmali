from smali.bridge import SmaliVM, SmaliObject

with open('example.smali', 'r', encoding='utf-8') as fp:
    source = fp.read()

vm = SmaliVM()
smali_class = vm.classloader.load_class(source, init=False)
smali_class.clinit()

instance = SmaliObject(smali_class)
instance.init()

toString = instance.smali_class.method("toString")
value = toString(instance)

print(value)
