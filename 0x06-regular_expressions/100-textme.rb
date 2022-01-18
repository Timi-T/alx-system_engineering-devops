#!/usr/bin/env ruby
#check a file for sender, reciever and flags

sender = ARGV[0].scan(/\[from:\S+\]/).join
reciever = ARGV[0].scan(/\[to:\S+\]/).join
flags = ARGV[0].scan(/\[flags:\S+\]/).join

sender["[from:"] = ""
sender = sender.chop
reciever["[to:"] = ""
reciever = reciever.chop
flags["[flags:"] = ""
flags = flags.chop
puts "#{sender},#{reciever},#{flags}"
