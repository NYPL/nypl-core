const fs = require('fs')
const path = require('path')
const csvParse = require('csv-parse')
const argv = require('minimist')(process.argv.slice(2))

function exitWithUsage () {
  console.log('Usage: node parse-notes [CSVFILE]')
  process.exit()
}

function updateFieldMappingBib (cb) {
  const bibMappingPath = path.join('../../', 'recap-discovery/field-mapping-bib.json')
  console.log(`Updating ${bibMappingPath}`)

  const content = fs.readFileSync(bibMappingPath, 'utf8')
  let mapping = JSON.parse(content)
  mapping = cb(mapping)

  fs.writeFileSync(bibMappingPath, JSON.stringify(mapping, null, 2))
}

const csvPath = process.argv[2]
if (!csvPath || !fs.existsSync(csvPath)) exitWithUsage()

console.log(`Parsing ${csvPath}`, fs.existsSync(csvPath))

const content = fs.readFileSync(csvPath, 'utf8')

csvParse(content, {
  from: 2, // Start at line 2 (line 1 is header)
  trim: true // Trim each value
}, (err, data) => {
  if (err) throw err

  const result = data.reduce((mappings, row) => {
    // Make sure mapping defines subfields:
    if (!/\d+ .+/.test(row[0])) return mappings

    let [ , marc, subfields ] = row[0].match(/(\d+) (.*)/)
    subfields = subfields
      .split(/[, ]+/)
      .map((c) => c.replace(/^\$/, ''))
    const description = row[2]

    // Make sure not 'Local Note':
    if (description === 'Local Note') return mappings

    const mapping = {
      marc,
      subfields,
      description
    }
    mappings.push(mapping)
    return mappings
  }, [])

  if (argv.save) {
    updateFieldMappingBib((mapping) => {
      mapping.Note.paths = result
      return mapping
    })
  } else {
    console.log('Mappings: ', JSON.stringify(result, null, 2))
  }
})

