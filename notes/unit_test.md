当你继承`TestCase`后，类中就有对应的 验证方法

常用的有：
```properties
# 验证arg1和arg2是否相等，如果相等测试通过
self.assertEqual(arg1, arg2)

# 验证arg1和arg2是否是同一个类型
self.assertIsInstance(arg1, arg2)

# 验证arg1和arg2是否不相等，不相等测试通过
self.assertNotEqual(arg1, arg2)

# 验证arg1和arg2是否不是一个类型，不是一个类型测试通过
self.assertNotIsInstance(arg1, arg2)

# 验证arg1是否是None，是就通过
self.assertIsNone(arg1)

# 验证arg1是否小于arg2，小于就通过
self.assertLess(arg1, arg2)

# 验证arg1是否小于等于arg2，小于等于就通过
self.assertLessEqual(arg1, arg2)

# 验证arg1是否是True，是就通过
self.assertTrue(arg1)

# 验证arg1是否大于arg2，大于就通过
self.assertGreater(arg1, arg2)

# 验证arg1是否大于等于arg2，大于等于就通过
self.assertGreaterEqual(arg1, arg2)
```








