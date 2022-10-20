#!/usr/bin/env ruby
text = ARGV[0].scan(/\[from:([\d\w]+)\] \[to:(.?\d+)\] \[flags:(.+-1)\]/)[0]
puts "#{text[0]},#{text[1]},#{text[2]}"
