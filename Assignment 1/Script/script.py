import m5
from caches       import *
from m5.objects   import *
from gem5.runtime import get_runtime_isa

system = System()

# Set the clock frequency of the system
system.clk_domain                = SrcClockDomain()
system.clk_domain.clock          = "1GHz"
system.clk_domain.voltage_domain = VoltageDomain()

# Set up the system
system.mem_mode   = "timing"              # Use timing accesses
system.mem_ranges = [AddrRange("512MB")]  # Create an address range

# Create a simple CPU
system.cpu = X86TimingSimpleCPU()

# Create an L1 instruction and data cache
system.cpu.icache = L1ICache()
system.cpu.dcache = L1DCache()

# Connect the instruction and data caches to the CPU
system.cpu.icache.connectCPU(system.cpu)
system.cpu.dcache.connectCPU(system.cpu)

# Create a memory bus, a coherent crossbar, in this case and Hook the CPU ports up to the l2bus
system.l2bus = L2XBar()
system.cpu.icache.connectBus(system.l2bus)
system.cpu.dcache.connectBus(system.l2bus)

# Create an L2 cache and connect it to the l2bus
system.l2cache = L2Cache()
system.l2cache.connectCPUSideBus(system.l2bus)

# Create a memory bus and Connect the L2 cache to the membus
system.membus = SystemXBar()
system.l2cache.connectMemSideBus(system.membus)

# create the interrupt controller for the CPU
system.cpu.createInterruptController()
system.cpu.interrupts[0].pio           = system.membus.mem_side_ports
system.cpu.interrupts[0].int_requestor = system.membus.cpu_side_ports
system.cpu.interrupts[0].int_responder = system.membus.mem_side_ports

# Connect the system up to the membus
system.system_port = system.membus.cpu_side_ports

# Create a DDR3 memory controller
system.mem_ctrl            = MemCtrl()
system.mem_ctrl.dram       = DDR3_1600_8x8()
system.mem_ctrl.dram.range = system.mem_ranges[0]
system.mem_ctrl.port       = system.membus.mem_side_ports

system.workload = SEWorkload.init_compatible("/home/shubham21099/CA/Assignment_1/Inputs/qsort_small")

# Created a process for a simple qsort_small application which takes input from input_small.dat file
process     = Process()
process.cmd = ["/home/shubham21099/CA/Assignment_1/Inputs/qsort_small", "/home/shubham21099/CA/Assignment_1/Inputs/input_small.dat"]

# Set the cpu to use the process as its workload and create thread contexts
system.cpu.workload = process
system.cpu.createThreads()

# Set up the root and start the simulation by setting full_system = False
root = Root(full_system = False, system = system)
m5.instantiate()
print("Beginning simulation!")
exit_event = m5.simulate()
print("Exiting @ tick %i because %s" % (m5.curTick(), exit_event.getCause()))