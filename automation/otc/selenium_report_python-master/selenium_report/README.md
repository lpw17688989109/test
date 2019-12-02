# �Ż�html����

Ϊ������С���ĸ��ֱ�̬����Ϊ��װ����ʾ�Ƹ�Ϊ���ñ�����Ӹߴ��ϣ����Ա������������Ż���

- ���Ա���������ʾ���Ż�һЩ����ʧ��������������
- ���������ʧ�ܽ�ͼ��չʾ��html������
- �Ż������ͼ�Ŵ���������
- ���ӱ�ͼͳ��
- ʧ�ܺ����Թ���
- ����python2.x ��3.x

# ����Ч��

1.���ɵĲ��Ա���Ч������ͼ��Ĭ��չʾ������쳣��������ʧ�����Ե��������Ҳ��ͳ�ƽ�ȥ��

![image](http://note.youdao.com/yws/api/personal/file/E97A193B84B6450FA7CA7E148EE98FF8?method=download&shareKey=735b747a3614590f9c97aa765647c3a1)

2.�����ʾ��ͼ������ֱ����ʾ��ȡ��ͼƬ�����豣�浽����
![image](http://note.youdao.com/yws/api/personal/file/FFC30301995F47B9AF7DD0F5D216C53C?method=download&shareKey=8c7ae911502c1f38e7b2ee541d13782d)

# table���

1.�޸ı���td�������ݣ������Զ���������

2.drawCircle������������ɱ�ͼ����

```html
<tr id='header_row'>
    <td>������/��������</td>
    <td>����</td>
    <td>ͨ��</td>
    <td>ʧ��</td>
    <td>����</td>
    <td>��ͼ</td>
    <td>�����ͼ</td>
</tr>
%(test_list)s
<tr id='total_row'>
    <td>ͳ��</td>
    <td>%(count)s</td>
    <td>%(Pass)s</td>
    <td>%(fail)s</td>
    <td>%(error)s</td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
</tr>
</table>
<script>
    drawCircle(%(Pass)s, %(fail)s, %(error)s)
</script>
```

# �쳣��ͼ

1.�����������ʧ�ܺ󣬻��Զ���ͼ�ģ�ͼƬ��base64��ʽ�洢��html�������棬���豣�浽����

> driver.get_screenshot_as_base64()

```python
    def addError(self, test, err):
        self.error_count += 1
        self.status = 1
        TestResult.addError(self, test, err)
        _, _exc_str = self.errors[-1]
        output = self.complete_output()
        self.result.append((2, test, output, _exc_str))
        try:
            driver = getattr(test, "driver")
            test.img = driver.get_screenshot_as_base64()
        except AttributeError:
            test.img = ""
        if self.verbosity > 1:
            sys.stderr.write('E  ')
            sys.stderr.write(str(test))
            sys.stderr.write('\n')
        else:
            sys.stderr.write('E')
```
2.��һ�����Ҫע�⣬����Ҫ����driver�������磺

```
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox()
```

# ʧ������

1.���ɱ���Ĳ����������һ������retry=1,�����ʾ����ʧ�ܺ󣬻�������һ�Ρ�
```python
# coding:utf-8

import HTMLTestRunner_jpg
import unittest

if __name__ == "__main__":
    discover = unittest.defaultTestLoader.discover("case","test*.py")
    print(discover)
    
    run = HTMLTestRunner_jpg.HTMLTestRunner(title="����װ�ƵĲ��Ա���",
                                            description="���Խ��",
                                            stream=open("result.html","wb"),
                                            verbosity=2,
                                            retry=1)
    
    run.run(discover)
```
2.verbosity=2��������ǿ���̨��ʾ���Խ������������֣�
```
E  test_01 (pject.test_jpg.Test1)
retesting... 1
E  test_01 (pject.test_jpg.Test1)
F  test_02 (pject.test_jpg.Test1)
retesting... 1
F  test_02 (pject.test_jpg.Test1)
ok test_03 (pject.test_jpg.Test1)
ok test_01 (pject.test_xxx.Test1)
ok test_02 (pject.test_xxx.Test1)

Time Elapsed: 0:00:17.892222
```
3.retesting���Ǵ������ܵ�����

# �ο�����github

[����github������](https://github.com/GoverSky/HTMLTestRunner)

������ڴ���Ļ�������΢����һ���ͼƬ��ʾ���Ż���֮ǰ��ͼƬ̫С����ʾģ�����Ŵ����£�Ȼ�������������£���������ִ�������ķ�ʽ
