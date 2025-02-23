#!/usr/bin/env ruby

# Requirement for part6 Ruby Metaprogramming
# Susanne Peer SWD21

#year = $stdin.read
#year.strip!

#### START of my CODE ####

at_exit { puts "Done" }

class A
  def self.inherited(subcl)
    print "Inherited,#{Time.now.year} by FH JOANNEUM Kapfenberg,"
  end

  def initialize
    print "Created,"
  end
end

class String
  def about
    return "#{self} by FH JOANNEUM Kapfenberg"
  end
end

#### END of my CODE ####   

about = A.new

class B < A
end

#puts "#{year.to_i}"
