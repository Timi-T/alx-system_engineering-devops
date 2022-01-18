#!/usr/bin/env ruby
#starts and ends with

puts ARGV[0].scan(/\A\d\d{8}\d\z/).join
