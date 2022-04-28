"""
find all files *.xml
find all files > 5mb
"""

from abc import ABC, abstractmethod
from typing import List


class Entry:
  """一个文件系统中的项，可能是文件或者文件夹
  """
  def __init__(self, name: str, is_dir: bool, children: List, size: int):
    self.name = name
    self.is_dir = is_dir
    self.children: List[Entry] = children
    self.size = size

  def __repr__(self):
    """格式化一下 print 的输出
    """
    output = f"[name={self.name}, is_dir={self.is_dir}, size={self.size}]"
    for c in self.children:
      output += f"\n ----{c.__repr__()}"
    return output


class Filter(ABC):
  """filter 抽象类
  """
  @abstractmethod
  def test(self, entry: Entry):
    pass

class FileExtensionFilter(Filter):
  """扩展名 filter
  """

  def __init__(self, extension: str):
    self.required_extension = extension

  def test(self, entry: Entry):
    if entry.is_dir:
      return False
    splited_filename = entry.name.split(".")
    if len(splited_filename) < 2:
      return False
    entry_extension = splited_filename[-1]
    return self.required_extension == entry_extension

class SizeFilter(Filter):
  """ size filter 抽象类. 因为 size 的比较可以有 >, >=, =, <, <=
  但其实可以通过 > 和 = 就可以构造出所有的比较。例如
  >= -> > or =
  <= -> not >
  <  -> not (> or =)
  这种由基本的元素来组合的思想值得学习
  """

  def __init__(self, size: int):
    self.required_size = size

  @abstractmethod
  def test(self, entry: Entry):
    pass

class SizeGreaterFilter(SizeFilter):
  """ 大于 size 的 filter
  """

  def __init__(self, size):
    super().__init__(size)

  def test(self, entry: Entry):
    return entry.size > self.required_size

class SizeEqualFilter(SizeFilter):
  """ 等于 size 的 filter
  """

  def __init__(self, size):
    super().__init__(size)

  def test(self, entry: Entry):
    return entry.size == self.required_size

class SizeGreaterOrEqualFilter(SizeFilter):
  """ SizeGreaterOrEqualFilter 是 SizeGreaterFilter 和 SizeEqualFilter 的组合
  """

  def __init__(self, size):
    super().__init__(size)
    self.greater_filter = SizeGreaterFilter(size)
    self.equal_filter = SizeEqualFilter(size)

  def test(self, entry: Entry):
    return self.greater_filter.test(entry) or self.equal_filter.test(entry)

class SizeLessOrEqualFilter(SizeFilter):
  """ SizeLessOrEqualFilter 是 SizeGreaterFilter 取反
  """

  def __init__(self, size):
    super().__init__(size)
    self.greater_filter = SizeGreaterFilter(size)

  def test(self, entry: Entry):
    return not self.greater_filter.test(entry)

class SizeLessFilter(SizeFilter):
  """ SizeLessOrEqualFilter 是 SizeGreaterOrEqualFilter 取反
  """

  def __init__(self, size):
    super().__init__(size)
    self.greater_or_equal_filter = SizeGreaterOrEqualFilter(size)

  def test(self, entry: Entry):
    return not self.greater_or_equal_filter.test(entry)


class Context: # Search
  """本次搜索执行的上下文
  :param entrypoint: 搜索的起始 entry
  :param filters: 搜索的过滤条件
  """

  def __init__(self, entrypoint: Entry, filters: List[Filter] = []):
    self.entrypoint = entrypoint
    self.filters = filters

  def add_filter(self, filter: Filter):
    self.filters.append(filter)

  def execute(self) -> List[Entry]:
    """bfs 搜索所有可能满足条件的 entry
    """
    results = []
    source = [self.entrypoint]
    while source:
      entry = source.pop()
      # if all([f.test(entry) for f in self.filters]):
      #   results.append(entry)
      # if entry.is_dir:
      #   source.extend(entry.children)
      if entry.is_dir:
        source.extend(entry.children)
      else:
        if all([f.test(entry) for f in self.filters]):
          results.append(entry)
    return results

# 这里直接手工构造目录和过滤条件了。 因为这不是 ood 的重点
# 过滤条件在实际使用中，一般是通过命令行传入的参数构造的，可以用 argparse 来解析命令行参数
"""
手动构造的目录结构大概长这样
├── code
│   └── main.py
│   └── cmd.go
│   └── data.json
"""
pyE = Entry("main.py", False, [], 20)
goE = Entry("cmd.go", False, [], 30)
jsonE = Entry("data.json", False, [], 256)
codeE = Entry("code", True, [pyE, goE, jsonE], 0)

context = Context(entrypoint=codeE)

# size 大于等于30的 filter
greater_or_equal_filter = SizeLessOrEqualFilter(30)
context.add_filter(greater_or_equal_filter)
print(context.execute())

# 以 .go 结尾的文件
file_extension_filter = FileExtensionFilter("go")
context.add_filter(file_extension_filter)
# context 里有两个 filter，所以只打印 size >= 30 并且扩展名为 go 的文件
print(context.execute())
