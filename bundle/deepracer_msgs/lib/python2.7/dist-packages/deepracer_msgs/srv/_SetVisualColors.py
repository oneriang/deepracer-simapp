# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from deepracer_msgs/SetVisualColorsRequest.msg. Do not edit."""
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct

import std_msgs.msg

class SetVisualColorsRequest(genpy.Message):
  _md5sum = "52f74642913b71ec583802100623aef1"
  _type = "deepracer_msgs/SetVisualColorsRequest"
  _has_header = False #flag to mark the presence of a Header object
  _full_text = """string[] link_names
string[] visual_names
std_msgs/ColorRGBA[] ambients
std_msgs/ColorRGBA[] diffuses
std_msgs/ColorRGBA[] speculars
std_msgs/ColorRGBA[] emissives
bool block

================================================================================
MSG: std_msgs/ColorRGBA
float32 r
float32 g
float32 b
float32 a
"""
  __slots__ = ['link_names','visual_names','ambients','diffuses','speculars','emissives','block']
  _slot_types = ['string[]','string[]','std_msgs/ColorRGBA[]','std_msgs/ColorRGBA[]','std_msgs/ColorRGBA[]','std_msgs/ColorRGBA[]','bool']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       link_names,visual_names,ambients,diffuses,speculars,emissives,block

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(SetVisualColorsRequest, self).__init__(*args, **kwds)
      #message fields cannot be None, assign default values for those that are
      if self.link_names is None:
        self.link_names = []
      if self.visual_names is None:
        self.visual_names = []
      if self.ambients is None:
        self.ambients = []
      if self.diffuses is None:
        self.diffuses = []
      if self.speculars is None:
        self.speculars = []
      if self.emissives is None:
        self.emissives = []
      if self.block is None:
        self.block = False
    else:
      self.link_names = []
      self.visual_names = []
      self.ambients = []
      self.diffuses = []
      self.speculars = []
      self.emissives = []
      self.block = False

  def _get_types(self):
    """
    internal API method
    """
    return self._slot_types

  def serialize(self, buff):
    """
    serialize message into buffer
    :param buff: buffer, ``StringIO``
    """
    try:
      length = len(self.link_names)
      buff.write(_struct_I.pack(length))
      for val1 in self.link_names:
        length = len(val1)
        if python3 or type(val1) == unicode:
          val1 = val1.encode('utf-8')
          length = len(val1)
        buff.write(struct.pack('<I%ss'%length, length, val1))
      length = len(self.visual_names)
      buff.write(_struct_I.pack(length))
      for val1 in self.visual_names:
        length = len(val1)
        if python3 or type(val1) == unicode:
          val1 = val1.encode('utf-8')
          length = len(val1)
        buff.write(struct.pack('<I%ss'%length, length, val1))
      length = len(self.ambients)
      buff.write(_struct_I.pack(length))
      for val1 in self.ambients:
        _x = val1
        buff.write(_get_struct_4f().pack(_x.r, _x.g, _x.b, _x.a))
      length = len(self.diffuses)
      buff.write(_struct_I.pack(length))
      for val1 in self.diffuses:
        _x = val1
        buff.write(_get_struct_4f().pack(_x.r, _x.g, _x.b, _x.a))
      length = len(self.speculars)
      buff.write(_struct_I.pack(length))
      for val1 in self.speculars:
        _x = val1
        buff.write(_get_struct_4f().pack(_x.r, _x.g, _x.b, _x.a))
      length = len(self.emissives)
      buff.write(_struct_I.pack(length))
      for val1 in self.emissives:
        _x = val1
        buff.write(_get_struct_4f().pack(_x.r, _x.g, _x.b, _x.a))
      buff.write(_get_struct_B().pack(self.block))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    try:
      if self.ambients is None:
        self.ambients = None
      if self.diffuses is None:
        self.diffuses = None
      if self.speculars is None:
        self.speculars = None
      if self.emissives is None:
        self.emissives = None
      end = 0
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.link_names = []
      for i in range(0, length):
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        start = end
        end += length
        if python3:
          val1 = str[start:end].decode('utf-8')
        else:
          val1 = str[start:end]
        self.link_names.append(val1)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.visual_names = []
      for i in range(0, length):
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        start = end
        end += length
        if python3:
          val1 = str[start:end].decode('utf-8')
        else:
          val1 = str[start:end]
        self.visual_names.append(val1)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.ambients = []
      for i in range(0, length):
        val1 = std_msgs.msg.ColorRGBA()
        _x = val1
        start = end
        end += 16
        (_x.r, _x.g, _x.b, _x.a,) = _get_struct_4f().unpack(str[start:end])
        self.ambients.append(val1)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.diffuses = []
      for i in range(0, length):
        val1 = std_msgs.msg.ColorRGBA()
        _x = val1
        start = end
        end += 16
        (_x.r, _x.g, _x.b, _x.a,) = _get_struct_4f().unpack(str[start:end])
        self.diffuses.append(val1)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.speculars = []
      for i in range(0, length):
        val1 = std_msgs.msg.ColorRGBA()
        _x = val1
        start = end
        end += 16
        (_x.r, _x.g, _x.b, _x.a,) = _get_struct_4f().unpack(str[start:end])
        self.speculars.append(val1)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.emissives = []
      for i in range(0, length):
        val1 = std_msgs.msg.ColorRGBA()
        _x = val1
        start = end
        end += 16
        (_x.r, _x.g, _x.b, _x.a,) = _get_struct_4f().unpack(str[start:end])
        self.emissives.append(val1)
      start = end
      end += 1
      (self.block,) = _get_struct_B().unpack(str[start:end])
      self.block = bool(self.block)
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    :param buff: buffer, ``StringIO``
    :param numpy: numpy python module
    """
    try:
      length = len(self.link_names)
      buff.write(_struct_I.pack(length))
      for val1 in self.link_names:
        length = len(val1)
        if python3 or type(val1) == unicode:
          val1 = val1.encode('utf-8')
          length = len(val1)
        buff.write(struct.pack('<I%ss'%length, length, val1))
      length = len(self.visual_names)
      buff.write(_struct_I.pack(length))
      for val1 in self.visual_names:
        length = len(val1)
        if python3 or type(val1) == unicode:
          val1 = val1.encode('utf-8')
          length = len(val1)
        buff.write(struct.pack('<I%ss'%length, length, val1))
      length = len(self.ambients)
      buff.write(_struct_I.pack(length))
      for val1 in self.ambients:
        _x = val1
        buff.write(_get_struct_4f().pack(_x.r, _x.g, _x.b, _x.a))
      length = len(self.diffuses)
      buff.write(_struct_I.pack(length))
      for val1 in self.diffuses:
        _x = val1
        buff.write(_get_struct_4f().pack(_x.r, _x.g, _x.b, _x.a))
      length = len(self.speculars)
      buff.write(_struct_I.pack(length))
      for val1 in self.speculars:
        _x = val1
        buff.write(_get_struct_4f().pack(_x.r, _x.g, _x.b, _x.a))
      length = len(self.emissives)
      buff.write(_struct_I.pack(length))
      for val1 in self.emissives:
        _x = val1
        buff.write(_get_struct_4f().pack(_x.r, _x.g, _x.b, _x.a))
      buff.write(_get_struct_B().pack(self.block))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    try:
      if self.ambients is None:
        self.ambients = None
      if self.diffuses is None:
        self.diffuses = None
      if self.speculars is None:
        self.speculars = None
      if self.emissives is None:
        self.emissives = None
      end = 0
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.link_names = []
      for i in range(0, length):
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        start = end
        end += length
        if python3:
          val1 = str[start:end].decode('utf-8')
        else:
          val1 = str[start:end]
        self.link_names.append(val1)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.visual_names = []
      for i in range(0, length):
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        start = end
        end += length
        if python3:
          val1 = str[start:end].decode('utf-8')
        else:
          val1 = str[start:end]
        self.visual_names.append(val1)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.ambients = []
      for i in range(0, length):
        val1 = std_msgs.msg.ColorRGBA()
        _x = val1
        start = end
        end += 16
        (_x.r, _x.g, _x.b, _x.a,) = _get_struct_4f().unpack(str[start:end])
        self.ambients.append(val1)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.diffuses = []
      for i in range(0, length):
        val1 = std_msgs.msg.ColorRGBA()
        _x = val1
        start = end
        end += 16
        (_x.r, _x.g, _x.b, _x.a,) = _get_struct_4f().unpack(str[start:end])
        self.diffuses.append(val1)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.speculars = []
      for i in range(0, length):
        val1 = std_msgs.msg.ColorRGBA()
        _x = val1
        start = end
        end += 16
        (_x.r, _x.g, _x.b, _x.a,) = _get_struct_4f().unpack(str[start:end])
        self.speculars.append(val1)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.emissives = []
      for i in range(0, length):
        val1 = std_msgs.msg.ColorRGBA()
        _x = val1
        start = end
        end += 16
        (_x.r, _x.g, _x.b, _x.a,) = _get_struct_4f().unpack(str[start:end])
        self.emissives.append(val1)
      start = end
      end += 1
      (self.block,) = _get_struct_B().unpack(str[start:end])
      self.block = bool(self.block)
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
_struct_4f = None
def _get_struct_4f():
    global _struct_4f
    if _struct_4f is None:
        _struct_4f = struct.Struct("<4f")
    return _struct_4f
_struct_B = None
def _get_struct_B():
    global _struct_B
    if _struct_B is None:
        _struct_B = struct.Struct("<B")
    return _struct_B
# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from deepracer_msgs/SetVisualColorsResponse.msg. Do not edit."""
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct


class SetVisualColorsResponse(genpy.Message):
  _md5sum = "a0af81bf1f7c2eacb2693173f999072a"
  _type = "deepracer_msgs/SetVisualColorsResponse"
  _has_header = False #flag to mark the presence of a Header object
  _full_text = """bool success
string status_message
int8[] status
string[] messages
"""
  __slots__ = ['success','status_message','status','messages']
  _slot_types = ['bool','string','int8[]','string[]']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       success,status_message,status,messages

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(SetVisualColorsResponse, self).__init__(*args, **kwds)
      #message fields cannot be None, assign default values for those that are
      if self.success is None:
        self.success = False
      if self.status_message is None:
        self.status_message = ''
      if self.status is None:
        self.status = []
      if self.messages is None:
        self.messages = []
    else:
      self.success = False
      self.status_message = ''
      self.status = []
      self.messages = []

  def _get_types(self):
    """
    internal API method
    """
    return self._slot_types

  def serialize(self, buff):
    """
    serialize message into buffer
    :param buff: buffer, ``StringIO``
    """
    try:
      buff.write(_get_struct_B().pack(self.success))
      _x = self.status_message
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      length = len(self.status)
      buff.write(_struct_I.pack(length))
      pattern = '<%sb'%length
      buff.write(struct.pack(pattern, *self.status))
      length = len(self.messages)
      buff.write(_struct_I.pack(length))
      for val1 in self.messages:
        length = len(val1)
        if python3 or type(val1) == unicode:
          val1 = val1.encode('utf-8')
          length = len(val1)
        buff.write(struct.pack('<I%ss'%length, length, val1))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    try:
      end = 0
      start = end
      end += 1
      (self.success,) = _get_struct_B().unpack(str[start:end])
      self.success = bool(self.success)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.status_message = str[start:end].decode('utf-8')
      else:
        self.status_message = str[start:end]
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sb'%length
      start = end
      end += struct.calcsize(pattern)
      self.status = struct.unpack(pattern, str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.messages = []
      for i in range(0, length):
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        start = end
        end += length
        if python3:
          val1 = str[start:end].decode('utf-8')
        else:
          val1 = str[start:end]
        self.messages.append(val1)
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    :param buff: buffer, ``StringIO``
    :param numpy: numpy python module
    """
    try:
      buff.write(_get_struct_B().pack(self.success))
      _x = self.status_message
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      length = len(self.status)
      buff.write(_struct_I.pack(length))
      pattern = '<%sb'%length
      buff.write(self.status.tostring())
      length = len(self.messages)
      buff.write(_struct_I.pack(length))
      for val1 in self.messages:
        length = len(val1)
        if python3 or type(val1) == unicode:
          val1 = val1.encode('utf-8')
          length = len(val1)
        buff.write(struct.pack('<I%ss'%length, length, val1))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    try:
      end = 0
      start = end
      end += 1
      (self.success,) = _get_struct_B().unpack(str[start:end])
      self.success = bool(self.success)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.status_message = str[start:end].decode('utf-8')
      else:
        self.status_message = str[start:end]
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sb'%length
      start = end
      end += struct.calcsize(pattern)
      self.status = numpy.frombuffer(str[start:end], dtype=numpy.int8, count=length)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.messages = []
      for i in range(0, length):
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        start = end
        end += length
        if python3:
          val1 = str[start:end].decode('utf-8')
        else:
          val1 = str[start:end]
        self.messages.append(val1)
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
_struct_B = None
def _get_struct_B():
    global _struct_B
    if _struct_B is None:
        _struct_B = struct.Struct("<B")
    return _struct_B
class SetVisualColors(object):
  _type          = 'deepracer_msgs/SetVisualColors'
  _md5sum = '2b593b9606746213e8e7b797a0ade086'
  _request_class  = SetVisualColorsRequest
  _response_class = SetVisualColorsResponse
