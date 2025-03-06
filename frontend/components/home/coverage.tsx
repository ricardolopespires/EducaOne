"use client";

import { motion } from "framer-motion";

const Coverage = () => {
  const regions = [
    {
      id: "amazonas",
      letter: "A",
      name: "Amazonas",
      color: "bg-purple-500",
      position: "top-[20%] left-[30%]",
      stats: {
        condos: 150,
        revenue: "1.2M"
      }
    },
    {
      id: "para",
      letter: "B",
      name: "Pará",
      color: "bg-pink-500",
      position: "top-[35%] left-[40%]",
      stats: {
        condos: 180,
        revenue: "1.5M"
      }
    },
    {
      id: "goias",
      letter: "C",
      name: "Goiás",
      color: "bg-orange-500",
      position: "top-[45%] right-[45%]",
      stats: {
        condos: 220,
        revenue: "1.8M"
      }
    },
    {
      id: "minas",
      letter: "D",
      name: "Minas Gerais",
      color: "bg-yellow-500",
      position: "bottom-[35%] right-[35%]",
      stats: {
        condos: 350,
        revenue: "2.5M"
      }
    }
  ];

  const containerVariants = {
    hidden: { opacity: 0 },
    visible: { 
      opacity: 1,
      transition: {
        staggerChildren: 0.1
      }
    }
  };

  const itemVariants = {
    hidden: { scale: 0.8, opacity: 0 },
    visible: { 
      scale: 1, 
      opacity: 1,
      transition: {
        type: "spring",
        stiffness: 100
      }
    }
  };

  const lineVariants = {
    hidden: { pathLength: 0 },
    visible: { 
      pathLength: 1,
      transition: {
        duration: 1.5,
        ease: "easeInOut"
      }
    }
  };

  return (
    <section className="py-20 bg-gray-900">
      <div className="container mx-auto px-4">
        <div className="max-w-4xl mx-auto">
          {/* Header */}
          <motion.div 
            className="text-center mb-16"
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ duration: 0.6 }}
          >
            <h2 className="text-3xl md:text-4xl font-bold text-white mb-4">
              Presença Nacional
              <br />
              <span className="bg-gradient-to-r from-blue-400 to-teal-400 bg-clip-text text-transparent">
                De Norte a Sul do Brasil
              </span>
            </h2>
            <p className="text-gray-400 text-lg">
              Nossa plataforma está presente nos principais estados, 
              transformando a gestão de condomínios em todo o país
            </p>
          </motion.div>

          {/* Map Container */}
          <div className="relative aspect-[4/3] bg-gray-800/50 rounded-3xl p-8 overflow-hidden">
            {/* Background Grid */}
            <div className="absolute inset-0 grid grid-cols-12 gap-4 p-8 opacity-20">
              {Array.from({ length: 96 }).map((_, i) => (
                <div key={i} className="w-2 h-2 bg-gray-600 rounded-full" />
              ))}
            </div>

            {/* Brazil Map Shape */}
            <motion.div 
              className="relative h-full"
              variants={containerVariants}
              initial="hidden"
              animate="visible"
            >
              <div className="absolute inset-0 bg-gradient-to-br from-gray-700/50 to-gray-800/50 rounded-2xl" />
              
              {/* Region Markers */}
              {regions.map((region) => (
                <motion.div
                  key={region.id}
                  className={`absolute ${region.position}`}
                  variants={itemVariants}
                >
                  <div className="relative group">
                    {/* Marker */}
                    <div className={`w-12 h-12 ${region.color} rounded-2xl flex items-center justify-center text-white font-bold text-xl shadow-lg`}>
                      {region.letter}
                    </div>
                    
                    {/* Tooltip */}
                    <div className="absolute left-full ml-4 top-0 bg-white rounded-xl p-4 shadow-xl opacity-0 group-hover:opacity-100 transition-opacity duration-200 pointer-events-none min-w-[200px]">
                      <p className="font-semibold text-gray-900">{region.name}</p>
                      <div className="mt-2 space-y-1">
                        <p className="text-sm text-gray-600">
                          <span className="font-medium text-gray-900">{region.stats.condos}</span> condomínios
                        </p>
                        <p className="text-sm text-gray-600">
                          R$ <span className="font-medium text-gray-900">{region.stats.revenue}</span> em economia
                        </p>
                      </div>
                    </div>
                  </div>
                </motion.div>
              ))}

              {/* Connection Lines */}
              <svg className="absolute inset-0 w-full h-full" viewBox="0 0 100 100" preserveAspectRatio="none">
                {regions.map((region, index) => (
                  regions.slice(index + 1).map((target, i) => (
                    <motion.path
                      key={`${region.id}-${target.id}`}
                      d={`M ${index * 25 + 20},${index * 20 + 30} Q ${50},50 ${(index + i + 1) * 25 + 20},${(index + i + 1) * 20 + 30}`}
                      stroke="url(#lineGradient)"
                      strokeWidth="0.5"
                      fill="none"
                      variants={lineVariants}
                    />
                  ))
                ))}
                <defs>
                  <linearGradient id="lineGradient" x1="0%" y1="0%" x2="100%" y2="100%">
                    <stop offset="0%" stopColor="#60A5FA" stopOpacity="0.2" />
                    <stop offset="100%" stopColor="#2DD4BF" stopOpacity="0.2" />
                  </linearGradient>
                </defs>
              </svg>
            </motion.div>
          </div>

          {/* Stats */}
          <motion.div 
            className="grid grid-cols-3 gap-8 mt-12"
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ delay: 0.3, duration: 0.6 }}
          >
            <div className="text-center">
              <p className="text-4xl font-bold bg-gradient-to-r from-blue-400 to-teal-400 bg-clip-text text-transparent">
                27
              </p>
              <p className="text-gray-400 mt-1">Estados</p>
            </div>
            <div className="text-center">
              <p className="text-4xl font-bold bg-gradient-to-r from-blue-400 to-teal-400 bg-clip-text text-transparent">
                150+
              </p>
              <p className="text-gray-400 mt-1">Cidades</p>
            </div>
            <div className="text-center">
              <p className="text-4xl font-bold bg-gradient-to-r from-blue-400 to-teal-400 bg-clip-text text-transparent">
                1.5M+
              </p>
              <p className="text-gray-400 mt-1">Moradores</p>
            </div>
          </motion.div>
        </div>
      </div>
    </section>
  );
};

export default Coverage; 