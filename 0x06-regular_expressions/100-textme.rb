#!/usr/bin/env ruby
#check a file for sender, reciever and flags

sender = ARGV[0].scan(/\[from:\S+\]/)
reciever = ARGV[0].scan(/\[to:\S+\]/)
flags = ARGV[0].scan(/\[flags:\S+\]/)

puts sender, ",", reciever, ",", flags
