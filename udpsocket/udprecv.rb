require 'socket'

# Agent で dnncls を起動

# d_agent = 
# f_agent = 

t = Thread.new do
  usv = UDPSocket.new
  usv.bind( "127.0.0.1", 20001 )
  while true
    
    ret = usv.recvfrom(256)
    
    puts ret[0].chomp
  end
end

while true
  line = gets
  break if line =~ /^q/
end

t.kill

# d_agent.puts("q")
# d_agent.close
#
# f_agent.puts("q")
# f_agent.close
