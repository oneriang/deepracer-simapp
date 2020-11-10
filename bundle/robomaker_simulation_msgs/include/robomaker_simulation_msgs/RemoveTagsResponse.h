// Generated by gencpp from file robomaker_simulation_msgs/RemoveTagsResponse.msg
// DO NOT EDIT!


#ifndef ROBOMAKER_SIMULATION_MSGS_MESSAGE_REMOVETAGSRESPONSE_H
#define ROBOMAKER_SIMULATION_MSGS_MESSAGE_REMOVETAGSRESPONSE_H


#include <string>
#include <vector>
#include <map>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>


namespace robomaker_simulation_msgs
{
template <class ContainerAllocator>
struct RemoveTagsResponse_
{
  typedef RemoveTagsResponse_<ContainerAllocator> Type;

  RemoveTagsResponse_()
    : success(false)
    , message()  {
    }
  RemoveTagsResponse_(const ContainerAllocator& _alloc)
    : success(false)
    , message(_alloc)  {
  (void)_alloc;
    }



   typedef uint8_t _success_type;
  _success_type success;

   typedef std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other >  _message_type;
  _message_type message;





  typedef boost::shared_ptr< ::robomaker_simulation_msgs::RemoveTagsResponse_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::robomaker_simulation_msgs::RemoveTagsResponse_<ContainerAllocator> const> ConstPtr;

}; // struct RemoveTagsResponse_

typedef ::robomaker_simulation_msgs::RemoveTagsResponse_<std::allocator<void> > RemoveTagsResponse;

typedef boost::shared_ptr< ::robomaker_simulation_msgs::RemoveTagsResponse > RemoveTagsResponsePtr;
typedef boost::shared_ptr< ::robomaker_simulation_msgs::RemoveTagsResponse const> RemoveTagsResponseConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::robomaker_simulation_msgs::RemoveTagsResponse_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::robomaker_simulation_msgs::RemoveTagsResponse_<ContainerAllocator> >::stream(s, "", v);
return s;
}

} // namespace robomaker_simulation_msgs

namespace ros
{
namespace message_traits
{



// BOOLTRAITS {'IsFixedSize': False, 'IsMessage': True, 'HasHeader': False}
// {'robomaker_simulation_msgs': ['/opt/workspace/AwsSilverstoneSimulationApplication/src/aws-robomaker-simulation-ros-pkgs/robomaker_simulation_msgs/msg'], 'std_msgs': ['/opt/ros/kinetic/share/std_msgs/cmake/../msg']}

// !!!!!!!!!!! ['__class__', '__delattr__', '__dict__', '__doc__', '__eq__', '__format__', '__getattribute__', '__hash__', '__init__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_parsed_fields', 'constants', 'fields', 'full_name', 'has_header', 'header_present', 'names', 'package', 'parsed_fields', 'short_name', 'text', 'types']




template <class ContainerAllocator>
struct IsFixedSize< ::robomaker_simulation_msgs::RemoveTagsResponse_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::robomaker_simulation_msgs::RemoveTagsResponse_<ContainerAllocator> const>
  : FalseType
  { };

template <class ContainerAllocator>
struct IsMessage< ::robomaker_simulation_msgs::RemoveTagsResponse_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::robomaker_simulation_msgs::RemoveTagsResponse_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::robomaker_simulation_msgs::RemoveTagsResponse_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::robomaker_simulation_msgs::RemoveTagsResponse_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::robomaker_simulation_msgs::RemoveTagsResponse_<ContainerAllocator> >
{
  static const char* value()
  {
    return "937c9679a518e3a18d831e57125ea522";
  }

  static const char* value(const ::robomaker_simulation_msgs::RemoveTagsResponse_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0x937c9679a518e3a1ULL;
  static const uint64_t static_value2 = 0x8d831e57125ea522ULL;
};

template<class ContainerAllocator>
struct DataType< ::robomaker_simulation_msgs::RemoveTagsResponse_<ContainerAllocator> >
{
  static const char* value()
  {
    return "robomaker_simulation_msgs/RemoveTagsResponse";
  }

  static const char* value(const ::robomaker_simulation_msgs::RemoveTagsResponse_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::robomaker_simulation_msgs::RemoveTagsResponse_<ContainerAllocator> >
{
  static const char* value()
  {
    return "\n\
bool success\n\
\n\
\n\
\n\
string message\n\
";
  }

  static const char* value(const ::robomaker_simulation_msgs::RemoveTagsResponse_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::robomaker_simulation_msgs::RemoveTagsResponse_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.success);
      stream.next(m.message);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct RemoveTagsResponse_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::robomaker_simulation_msgs::RemoveTagsResponse_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::robomaker_simulation_msgs::RemoveTagsResponse_<ContainerAllocator>& v)
  {
    s << indent << "success: ";
    Printer<uint8_t>::stream(s, indent + "  ", v.success);
    s << indent << "message: ";
    Printer<std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other > >::stream(s, indent + "  ", v.message);
  }
};

} // namespace message_operations
} // namespace ros

#endif // ROBOMAKER_SIMULATION_MSGS_MESSAGE_REMOVETAGSRESPONSE_H
